import pandas as pd


df = pd.read_csv("PYTH_07_01_Inventario.csv", sep=";")

# Cálculo do total por venda (adicionado ao DataFrame para reutilização)
df['PurchasePriceTotal'] = df['StockQuantity'] * df['PurchasePrice']
df['SalePriceTotal'] = df['StockQuantity'] * df['SalePrice']


# Função para exibir o DataFrame original e salvar como CSV
def mostrar_dataframe():
    print("\nDataFrame Original:\n")
    print(df.to_string(index=False))
    df.to_csv('dataframe_original.csv', index=False)
    print("Arquivo 'dataframe_original.csv' salvo com sucesso!")

# Função para exibir total por venda e salvar como CSV
def total_por_compra():
    print("\nTotal por compra:")
    for index, row in df.iterrows():
        print(f"Produto: {row['ProductName']}, Total: R$ {row['PurchasePriceTotal']:.2f}")
    df.to_csv('total_por_venda.csv', index=False)
    df.to_excel('total_por_venda.xlsx', index=False)
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

# Função para exibir produto mais caro e salvar como CSV
def produto_mais_caro():
    idx = df['Preço Uni'].idxmax()
    produto = df.loc[idx, 'Produto']
    preco = df.loc[idx, 'Preço Uni']
    print(f"\nProduto mais Caro: {produto} (Preço Unitário: R$ {preco:.2f})")
    df_produto = pd.DataFrame({'Produto': [produto], 'Preço Unitário': [preco]})
    df_produto.to_csv('produto_mais_caro.csv', index=False)
    print("Arquivo 'produto_mais_caro.csv' salvo com sucesso!")

# Função para exibir total geral de vendas e salvar como CSV
def total_geral_vendas():
    total = df['Total Venda'].sum()
    print(f"\nTotal Geral de Vendas: R$ {total:.2f}")
    df_total = pd.DataFrame({'Total Geral de Vendas': [total]})
    df_total.to_csv('total_geral_vendas.csv', index=False)
    print("Arquivo 'total_geral_vendas.csv' salvo com sucesso!")

# Função para exibir vendas com valor menor que 100 e salvar como CSV
def vendas_menor_100():
    vendas = df[df['Total Venda'] < 100]
    if vendas.empty:
        print("\nNenhuma venda com valor menor que R$ 100.00")
    else:
        print("\nVendas com valor menor que R$ 100.00:")
        for index, row in vendas.iterrows():
            print(f"Produto: {row['Produto']}, Quantidade: {row['Quantidade']}, Total: R$ {row['Total Venda']:.2f}")
        vendas_csv = vendas[['Produto', 'Quantidade', 'Total Venda']]
        vendas_csv.to_csv('vendas_menor_100.csv', index=False)
        print("Arquivo 'vendas_menor_100.csv' salvo com sucesso!")

# Função para exibir vendas ordenadas pela maior quantidade e salvar como CSV
def ordenar_por_quantidade():
    ordenado = df.sort_values(by='Quantidade', ascending=False)
    print("\nVendas Ordenadas pela Maior Quantidade Vendida:")
    for index, row in ordenado.iterrows():
        print(f"Produto: {row['Produto']}, Quantidade: {row['Quantidade']}, Total: R$ {row['Total Venda']:.2f}")
    ordenado_csv = ordenado[['Produto', 'Quantidade', 'Total Venda']]
    ordenado_csv.to_csv('ordenar_por_quantidade.csv', index=False)
    print("Arquivo 'ordenar_por_quantidade.csv' salvo com sucesso!")

# Dicionário de opções (adicionada nova opção 'h' para mostrar DataFrame)
opcoes = {
    'a': ("Total por Venda", total_por_compra),
    'b': ("Total de Vendas por Item", total_por_venda),
    'c': ("Produto mais Vendido", produto_mais_vendido),
    'd': ("Produto mais Caro", produto_mais_caro),
    'e': ("Total Geral de Vendas", total_geral_vendas),
    'f': ("Vendas com valor menor que 100", vendas_menor_100),
    'g': ("Ordenar por Quantidade Vendida", ordenar_por_quantidade),
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
