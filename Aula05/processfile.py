import pandas as pd 

df = pd.read_csv("PYTH_06_04_relatorio_vendas.csv")

reclassifica = df.sort_values(by="Vendedor", ascending=True)

nome_arquivo = "processfile_reclassificado.csv"

reclassifica.to_csv(nome_arquivo, index=False)

print(reclassifica.head())