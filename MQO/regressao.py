# Análise de regressão do consumo de iluminação pública
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV corretamente
df = pd.read_csv('MQO/Consumo_Tabela.csv', sep='\t', skiprows=2, encoding='utf-16')
# Renomear colunas para facilitar análise
df.columns = [
	'Municipio', 'Regiao', 'Total', 'Residencial', 'Industrial', 'Comercial', 'Rural',
	'Poder_Publico', 'Iluminacao_Publica', 'Servico_Publico', 'Consumo_Proprio',
	'Mercado_Cativo', 'Mercado_Livre'
]
print('Colunas renomeadas:', df.columns.tolist())
print('Primeiras linhas:')
print(df.head())

# Converter colunas numéricas (remover vírgulas e transformar em float)
for col in df.columns[2:]:
	df[col] = df[col].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
	df[col] = pd.to_numeric(df[col], errors='coerce')

# Análise exploratória
print('Resumo estatístico do consumo de iluminação pública:')
print(df['Iluminacao_Publica'].describe())

plt.figure(figsize=(12,6))
plt.plot(df['Municipio'], df['Iluminacao_Publica'], marker='o', linestyle='-')
plt.xticks(rotation=90, fontsize=8)
plt.title('Consumo de Iluminação Pública por Município (Série Temporal)')
plt.xlabel('Município')
plt.ylabel('Consumo de Iluminação Pública (MWh)')
plt.tight_layout()
plt.show()

# Correlação com outras variáveis
correlacoes = df.corr(numeric_only=True)['Iluminacao_Publica'].sort_values(ascending=False)
print('\nCorrelação do consumo de iluminação pública com outras variáveis:')
print(correlacoes)

# Regressão linear: Iluminação Pública ~ Total + Residencial + Industrial + Comercial + Rural + Poder Público
X = df[['Total', 'Residencial', 'Industrial', 'Comercial', 'Rural', 'Poder_Publico']]
y = df['Iluminacao_Publica']
X = sm.add_constant(X)
model = sm.OLS(y, X, missing='drop').fit()

print('\nResumo da regressão:')
print(model.summary())

# Gráfico de resíduos
plt.figure(figsize=(10,6))
sns.residplot(x=model.fittedvalues, y=model.resid, lowess=True)
plt.xlabel('Valores ajustados')
plt.ylabel('Resíduos')
plt.title('Resíduos da Regressão')
plt.show()
