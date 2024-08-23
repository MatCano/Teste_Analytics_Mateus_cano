import pandas as pd
import numpy as np

# SIMULAÇAO
np.random.seed(2)
data = {
    'ID': range(1, 301),
    'Data': pd.date_range(start='2023-01-01', periods=300, freq='D'),
    'Produto': np.random.choice(['Produto A', 'Produto B', 'Produto C'], 300),
    'Categoria': np.random.choice(['Categoria 1', 'Categoria 2'], 300),
    'Quantidade': np.random.randint(1, 20, 300),
    'Preço': np.random.uniform(10.0, 100.0, 300)
}
df = pd.DataFrame(data)
df['Valor Total'] = df['Quantidade'] * df['Preço']

# LIMPEZA
df.drop_duplicates(inplace=True)
df['Data'] = pd.to_datetime(df['Data'])

# DATASET LIMPO
df.to_csv('data/clean_sales.csv', index=False)

# ANALISE
total_vendas = df.groupby('Produto')['Valor Total'].sum()
produto_mais_vendido = total_vendas.idxmax()
produto_menos_vendido = total_vendas.idxmin()

print(f"Total de vendas por produto:\n{total_vendas}")
print(f"Produto com maior número de vendas totais: {produto_mais_vendido}")
print(f"Produto com menor número de vendas totais: {produto_menos_vendido}")
