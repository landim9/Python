def cota():
    aeroportos = {
    1: ("Congonhas-SP", 102),
    2: ("Guarulhos-SP", 112),
    3: ("Campo de Marte-SP", 98),
    4: ("Pinto Martins-CE", 2922),
    5: ("Eduardo Gomes-AM", 6294)
}

    print("\nAeroportos de destino disponíveis:")
    for num, (nome, distancia) in aeroportos.items():
            print(f"{num}. {nome} ({distancia} KM)")
        
    while True:  # Loop para repetir até uma entrada válida
        try:
            escolha = int(input("\nDigite o número do Aeroporto de Destino: "))
                
            if escolha in aeroportos:  # Verifica se o número está no dicionário
                    nome_aeroporto, distancia = aeroportos[escolha]
                    print(f"Você escolheu: {nome_aeroporto} ({distancia} KM)")
                    break  # Sai do loop se a escolha for válida
            else:
                    print("Erro: Opção inválida. Tente novamente.")
        except ValueError:  # Captura apenas erros de conversão (ex: letras em vez de números)
                print("Valor inválido, tente novamente. Digite apenas números.")
    
    
    print("1. Caixa Papelão")
    print("2. Container")

    choice = input("Escolha uma opção: ")

    if choice == "1":
        try:
            y = float(input("Digite a largura em Mt (Metros): ").replace(",", "."))
            x = float(input("Digite a altura em Mt(Metros): ").replace(",", "."))
            z = float(input("Digite a profundidade em Mt(Metros): ").replace(",", "."))
            w = float(input("Digite o peso em Kg(Kilo): ").replace(",", "."))
            f = 0.26
            d = float(input("Digite a distancia em Km (Kilometros)").replace(",", ".")) 
            
            formula = ((y * x * z * w) * (1 + f) * (1+(d*9.8)) )
            
            print("Aeroporto: ", escolha)
            print(f"Custo estimado de frete: R$ {formula:.2f}")
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
    
    elif choice == "2":
        try:
            y = float(input("Digite a largura em Mt (Metros): ").replace(",", "."))
            x = float(input("Digite a altura em Mt(Metros): ").replace(",", "."))
            z = float(input("Digite a profundidade em Mt(Metros): ").replace(",", "."))
            w = float(input("Digite o peso em Kg(Kilo): ").replace(",", "."))
            f = 0.37
            d = float(input("Digite a distancia em Km (Kilometros)").replace(",", "."))
            
            formula = ((y * x * z * w) * (1 + f) * (1+(d*9.8)) )
            
            print(f"Custo estimado de frete: R$ {formula:.2f}")
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
    else:
        print("Valor invalido")