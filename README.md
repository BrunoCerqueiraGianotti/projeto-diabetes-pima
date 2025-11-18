📊 Análise do risco de diabetes tipo 2 em mulheres Pima (Akimel O’odham)
👥 Autores

Bruno Cerqueira Gianotti | RA: 10721759

Daniel Fernandes Saraiva | RA: 10381985

Gabrielle Solange Ferreira | RA: 10414956

Reginaldo Rogério de Campos | RA: 10743942

🧾 Descrição do Projeto

Este projeto investiga fatores associados ao risco de diabetes tipo 2 em mulheres Pima, um povo indígena norte-americano, utilizando o tradicional Pima Indians Diabetes Dataset.

O objetivo central é realizar uma análise exploratória detalhada, com limpeza, tratamento de dados, detecção de outliers, visualizações e identificação dos fatores mais correlacionados ao diagnóstico de diabetes (variável Outcome).

Este repositório faz parte da entrega do Projeto Aplicado I do curso de Banco de Dados.

🎯 Objetivo Geral

Aplicar conceitos fundamentais de Ciência de Dados para:

Analisar variáveis clínicas que influenciam o risco de diabetes

Tratar valores inconsistentes e ausentes adequadamente

Explorar relações entre fatores de saúde e o diagnóstico

Gerar visualizações de apoio

Preparar a base para futuros modelos preditivos

📁 Estrutura do Repositório

projeto-diabetes-pima/
│
├── README.md                         # Documentação principal do projeto
├── PDFs/
│   └── Projeto Aplicado I (A1).pdf   # Relatório completo
│
├── datasets/
│   └── pima_dataset.csv              # Base de dados utilizada
│
├── scripts/
│   └── eda_pima.py (futuro)          # Scripts de análise e modelagem
│
└── imagens/
    └── (gráficos gerados)            # Visualizações da EDA

📚 Sobre o Dataset

O conjunto de dados contém 768 registros de pacientes do sexo feminino, com variáveis como:

Gravidez

Glicose

Pressão sanguínea

Espessura da dobra cutânea

Insulina

IMC

Função genética da diabetes

Resultado (0 = não diabético, 1 = diabético)

Source original: National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK).

🛠️ Metodologia e Processamento dos Dados

O script principal realiza:

✔️ 1. Leitura e inspeção inicial

Dimensões

Tipos de variáveis

Estatísticas básicas

✔️ 2. Tratamento de valores inválidos

Substituição de valores 0 em colunas onde esse valor não é fisiologicamente plausível:

Glucose, BloodPressure, SkinThickness, Insulin, BMI


Esses zeros são convertidos para NaN.

✔️ 3. Imputação de valores ausentes

Estratégia híbrida:

Tipo de variável	Método
Variáveis centrais (Glucose, BloodPressure, BMI)	Mediana
Variáveis críticas e mais variáveis (SkinThickness, Insulin)	KNN Imputer
✔️ 4. Detecção e remoção de outliers

Usando Z-score com limiar de 3 desvios padrão.

✔️ 5. Análise Exploratória de Dados (EDA)

Inclui:

Distribuições individuais

Boxplots por diagnóstico

Avaliação da variável alvo

Heatmap de correlação

Pairplot com diferenciação por Outcome

✔️ 6. Identificação dos fatores mais correlacionados

Cálculo de correlação com a variável Outcome.

💻 Como Executar o Projeto
✔️ Requisitos

Instale as dependências:

pip install pandas numpy seaborn matplotlib scikit-learn scipy

✔️ Rodando no Google Colab

Faça upload do arquivo pima_dataset.csv

Copie e cole o script no notebook

Execute célula por célula

✔️ Rodando localmente
python seu_script.py

📊 Principais Visualizações

As imagens geradas pela análise (histogramas, boxplots, correlação etc.) estão na pasta:

/imagens


Exemplos:

Distribuição de glicose

Boxplot de IMC por diagnóstico

Heatmap de correlação

Pairplot segmentado por Outcome

(As imagens podem ser incorporadas futuramente ao README.)

🔎 Principais Insights da Análise

✔ Glicose foi a variável com maior correlação positiva com diabetes
✔ IMC e Insulina também mostraram forte associação
✔ Outliers foram identificados em variáveis como Insulin e SkinThickness
✔ Distribuição de Outcome é desbalanceada (maioria classe 0)
✔ A combinação de glicose alta + IMC elevado aparece frequentemente associada ao diagnóstico positivo

📌 Próximos passos

Adicionar modelagem preditiva (Regressão Logística, Random Forest, XGBoost)

Implementar validação cruzada

Criar dashboard interativo (Streamlit ou Power BI)

Refinar outliers com métodos robustos (IQR, LOF, Isolation Forest)

🔗 Link para o Repositório

https://github.com/BrunoCerqueiraGianotti/projeto-diabetes-pima
