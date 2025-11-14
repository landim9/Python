from pickletools import opcodes
import pandas as pd

df = pd.read_csv("PYTH_07_01_Inventario.csv", sep=";")

df['PurchasePriceTotal'] = df['StockQuantity'] * df['PurchasePrice']
df['SalePriceTotal'] = df['StockQuantity'] * df['SalePrice']


# Função para exibir o DataFrame original e salvar como CSV
def mostrar_dataframe():
    print("\nDataFrame Original:\n")
    print(df.to_string(index=False))
    df.to_csv('dataframe_original.csv', index=False)
    print("Arquivo 'dataframe_original.csv' salvo com sucesso!")

def total_por_compra():
    print("\nTotal por compra:")
    for index, row in df.iterrows():
        print(f"Produto: {row['ProductName']}, Total: R$ {row['PurchasePriceTotal']:.2f}")
    df.to_csv('total_por_venda.csv', index=False)
    print("Arquivo 'total_por_venda.csv' salvo com sucesso!")

# Função para exibir total de vendas por item e salvar como CSV
def total_por_venda():
    print("\nTotal por Venda:")
    for index, row in df.iterrows():
        print(f"Produto: {row['ProductName']}, Total: R$ {row['SalePriceTotal']:.2f}")
    df_total = df[['ProductName', 'SalePriceTotal']]
    df_total.to_csv('total_por_venda.csv', index=False)
    print("Arquivo 'total_por_venda.csv' salvo com sucesso!")

# Função para exibir produto mais vendido e salvar como CSV
def produto_mais_vendido():
    produto = df.groupby('Produto')['Quantidade'].sum().idxmax()
    quantidade = df.groupby('Produto')['Quantidade'].sum().max()
    print(f"\nProduto mais Vendido: {produto} (Quantidade Total: {quantidade})")
    df_produto = pd.DataFrame({'Produto': [produto], 'Quantidade Total': [quantidade]})
    df_produto.to_csv('produto_mais_vendido.csv', index=False)
    print("Arquivo 'produto_mais_vendido.csv' salvo com sucesso!")

opcoes = {
    'a': ("Total por Venda", total_por_venda),
    'b': ("Total de Vendas por Item", total_por_compra),
    'c': ("Produto mais Vendido", produto_mais_vendido),
    'h': ("Mostrar DataFrame Original", mostrar_dataframe),
}
    
# Função para mostrar o menu (aprimorada com f-strings e separadores visuais)
def mostrar_menu():
    print("\n" + "=" * 60)
    print("Sistema de Análise de Vendas - Escolha uma opção:")
    for key, (descricao, _) in opcoes.items():
        print(f"  {key.upper()}) {descricao}")
    print("  S) Sair")
    print("=" * 60)

# Loop principal (aprimorado com validação de entrada e mensagens mais claras)
while True:
    mostrar_menu()
    escolha = input("Digite a opção desejada: ").lower().strip()

    if escolha == 's':
        print("\nPrograma Finalizado. Obrigado por usar o sistema!")
        break
    elif escolha in opcoes:
        print("-" * 60)
        opcoes[escolha][1]()  # Executa a função correspondente
        print("-" * 60)
        input("Pressione Enter para continuar...")  # Pausa para melhor interação

    else:
        print("\nOpção inválida! Por favor, tente novamente com uma das opções listadas.")
