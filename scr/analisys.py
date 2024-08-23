import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# estava dando erro achei essa linha no stackoverflow e funcionou pode ser coisa do linux não ter funcionado
plt.switch_backend('Agg') # não sei ao certo o que isso faz

# pegando o dataset
df = pd.read_csv('data/clean_sales.csv')

# converter a coluna 'data' para datetime
df['Data'] = pd.to_datetime(df['Data'])

# vendas ao longo do tempo
df['Mês'] = df['Data'].dt.to_period('M')
vendas_mensais = df.groupby('Mês')['Valor Total'].sum()

plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o')
plt.title('Tendência de Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Valor Total de Vendas')
plt.grid(True)
plt.savefig('vendas_mensais.png')  # salvar o gráfico como imagem
plt.close()

# plotando um gráfico de distribuiçao de vendas de cada produto
plt.figure(figsize=(12, 6))
sns.boxplot(x='Produto', y='Valor Total', data=df)
plt.title('Distribuição de Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Valor Total de Vendas')
plt.savefig('boxplot_vendas_produto.png')  # salvar o gráfico como imagem
plt.close()

# transformando esses dados em numeros mais palpáveis
print("Resumo Estatístico das Vendas por Produto:")
print(df.groupby('Produto')['Valor Total'].describe())

# padrões ou insights interessantes
print("\nPadrões ou Insights Interessantes:")
print("1. Produto mais vendido:", df.groupby('Produto')['Valor Total'].sum().idxmax())
print("2. Produto menos vendido:", df.groupby('Produto')['Valor Total'].sum().idxmin())
print("3. Mês com maior valor de vendas:", vendas_mensais.idxmax())
print("4. Mês com menor valor de vendas:", vendas_mensais.idxmin())
