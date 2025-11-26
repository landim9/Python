import pandas as pd

url = "https://raw.githubusercontent.com/JansenLeite/Python/main/PYTH_07_01_Inventario.csv"

# Carregar dados
df = pd.read_csv(url, sep=";")

df["PurchasePriceTotal"] = df["PurchasePrice"] * df["StockQuantity"]
df["SalePriceTotal"] = df["SalePrice"] * df["StockQuantity"]

df.to_csv("inventario_totais.csv", index=False)
df.to_excel("inventario_totais.xlsx", index=False)

df_fornecedor = df.groupby("Supplier").sum(numeric_only=True).reset_index()
df_fornecedor = df_fornecedor.sort_values("Supplier")
df_fornecedor.to_csv("inventario_fornecedores.csv", index=False)
df_fornecedor.to_excel("inventario_fornecedores.xlsx", index=False)

df_acima60 = df[df["StockQuantity"] > 60]
df_acima60.to_csv("inventario_acima60.csv", index=False)
df_acima60.to_excel("inventario_acima60.xlsx", index=False)

print("Arquivos gerados...")