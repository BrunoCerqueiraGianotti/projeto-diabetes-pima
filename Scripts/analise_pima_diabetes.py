# ============================================================
# Análise de Dados - Pima Indians Diabetes Dataset
# ============================================================
# Este script realiza:
# 1. Leitura e limpeza dos dados
# 2. Tratamento de valores ausentes e incorretos
# 3. Análise Exploratória de Dados (EDA)
# 4. Visualizações para entender relações entre variáveis e diabetes
# ============================================================

# ===================== BIBLIOTECAS ==========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import KNNImputer
from scipy import stats

# ===================== LEITURA DOS DADOS ====================
# Substitua pelo caminho do seu arquivo no Colab
# Ex: df = pd.read_csv('/content/pima_dataset.csv')
df = pd.read_csv('pima_dataset.csv')

print("Dimensões do dataset:", df.shape)
print("\nVisualização inicial:")
print(df.head())

# ===================== INFORMAÇÕES BÁSICAS ==================
print("\nInformações gerais:")
print(df.info())

print("\nResumo estatístico:")
print(df.describe())

# ===================== AJUSTE DE VALORES INCORRETOS ==========
# Algumas colunas não devem ter valor 0 (ex: pressão, glicose, IMC)
cols_invalidas = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in cols_invalidas:
    df[col] = df[col].replace(0, np.nan)

print("\nValores ausentes após substituição dos zeros incorretos:")
print(df.isna().sum())

# ===================== TRATAMENTO DE VALORES FALTANTES ======
# Estratégia mista: média, mediana, moda, e KNN

# 1. Substituir colunas com poucos nulos pela mediana
for col in ['Glucose', 'BloodPressure', 'BMI']:
    df[col].fillna(df[col].median(), inplace=True)

# 2. Substituir colunas mais críticas pelo KNN
imputer = KNNImputer(n_neighbors=5)
df[['SkinThickness', 'Insulin']] = imputer.fit_transform(df[['SkinThickness', 'Insulin']])

print("\nValores ausentes após imputação:")
print(df.isna().sum())

# ===================== DETECÇÃO DE OUTLIERS =================
# Usando o método do Z-score
z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
df_sem_outliers = df[(z_scores < 3).all(axis=1)]
print(f"\nRemovidos {df.shape[0] - df_sem_outliers.shape[0]} outliers.")

df = df_sem_outliers

# ===================== ANÁLISE EXPLORATÓRIA =================
print("\nDistribuição da variável alvo (Outcome):")
print(df['Outcome'].value_counts())

plt.figure(figsize=(5,4))
sns.countplot(data=df, x='Outcome', palette='Set2')
plt.title('Distribuição de Casos de Diabetes (0 = Não, 1 = Sim)')
plt.show()

# Histograma e boxplots
df.hist(bins=20, figsize=(14,10), color='teal')
plt.suptitle('Distribuição das Variáveis Numéricas')
plt.show()

# Boxplots por diabetes
plt.figure(figsize=(14,10))
for i, col in enumerate(df.columns[:-1]):
    plt.subplot(3,3,i+1)
    sns.boxplot(x='Outcome', y=col, data=df, palette='Set2')
    plt.title(col)
plt.tight_layout()
plt.show()

# ===================== CORRELAÇÕES ===========================
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='viridis', fmt=".2f")
plt.title('Matriz de Correlação')
plt.show()

# ===================== INSIGHTS ==============================
corr_target = df.corr()['Outcome'].sort_values(ascending=False)
print("\nCorrelação das variáveis com o diabetes:")
print(corr_target)

# ===================== RELAÇÕES ESPECÍFICAS ==================
sns.pairplot(df, hue='Outcome', diag_kind='kde', corner=True, palette='husl')
plt.suptitle('Relação entre Variáveis e Diagnóstico de Diabetes', y=1.02)
plt.show()

print("\nAnálise concluída com sucesso!")
