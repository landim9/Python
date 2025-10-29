import locale
def calculadora():
    try:
        oper = input("Digite o operador (+, -, *, /, %): ")
        num1 = float(input("\nDigite o primeiro número: "))
        num2 = float(input("\nDigite o segundo número: "))
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Erro: Divisão por zero!"
        elif oper == "%":
            result = (num1 / 100) * num2
        else:
            result = "Erro: Operador inválido!"
        
        print(f"Resultado: {result}")
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")

def cota():
    aeroportos = {
        1: ("Congonhas-SP", 102),
        2: ("Guarulhos-SP", 112),
        3: ("Campo de Marte-SP", 98),
        4: ("Pinto Martins-CE", 2922),
        5: ("Eduardo Gomes-AM\n", 6294)
    }

    
    print("Aeroportos de destino disponíveis:")
    for num, (nome, distancia) in aeroportos.items():
        print(f"{num}. {nome} ({distancia} KM)")
    
    while True:  
        try:
            escolha = int(input("\nDigite o número do Aeroporto de Destino: "))
            
            if escolha in aeroportos:  
                nome_aeroporto, distancia = aeroportos[escolha]  
                print(f"Você escolheu: {nome_aeroporto} ({distancia} KM)")
                break  
            else:
                print("Erro: Opção inválida. Tente novamente.")
        except ValueError:  
            print("Valor inválido, tente novamente. Digite apenas números.")
    
    
    print("\n1. Caixa Papelão")
    print("\n2. Container")
    
    choice = input("Escolha uma opção: ")
    
    if choice == "1":
        try:
            y = float(input("\nDigite a largura em Mt (Metros): ").replace(",", "."))
            x = float(input("\nDigite a altura em Mt (Metros): ").replace(",", "."))
            z = float(input("\nDigite a profundidade em Mt (Metros): ").replace(",", "."))
            w = float(input("\nDigite o peso em Kg (Kilo): ").replace(",", "."))
            f = 0.26  
            t = int(input("\nDigite o total de itens: "))
            
            formula = ((y * x * z * w) * (1 + f) * (1 + (distancia * 9.8)) * t)  
            
            
            formatted_formula = locale.format_string('%.2f', formula, grouping=True)
            print("\nAeroporto: ", nome_aeroporto)  
            print(f"\nCusto estimado de frete: R$ {formatted_formula}")
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
    
    elif choice == "2":
        try:
            y = float(input("\nDigite a largura em Mt (Metros): ").replace(",", "."))
            x = float(input("\nDigite a altura em Mt (Metros): ").replace(",", "."))
            z = float(input("\nDigite a profundidade em Mt (Metros): ").replace(",", "."))
            w = float(input("\nDigite o peso em Kg (Kilo): ").replace(",", "."))
            f = 0.37  
            t = int(input("\nDigite o total de itens: "))
            
            formula = ((y * x * z * w) * (1 + f) * (1 + (distancia * 9.8)) * t)  

            formatted_formula = locale.format_string('%.2f', formula, grouping=True)
            print("\nAeroporto: ", nome_aeroporto)  
            print(f"\nCusto estimado de frete: R$ {formatted_formula}\n")
        except ValueError:
            print("Erro: Entrada inválida. Certifique-se de digitar números válidos.")
    else:
        print("Valor inválido")

if __name__ == "__main__":
    user = "admin"
    password = "senha123"

    while True:
        print("\nBem-vindo ao Cotafrete! Por favor, faça login.")    
        print("-" * 20)
        username = input("\nUsuário: ")
        password = input("\nSenha: ")

        if username == user and password == password:
            print("Login bem-sucedido!")   
            print("Entrando no menu...")  # Mensagem de depuração
            break 
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
    
    while True:
        print("\nCOTAFRETE")
        print("-" * 20)
        print("\nMenu")
        print("\n1. Calculadora")
        print("\n2. Cotação de Frete")
        print("\n3. Finalizar o Programa")
                    
        choice = input("\nEscolha uma opção: ")
                    
        if choice == '1':
            calculadora()   
        elif choice == '2':
            cota()      
        elif choice == '3':
            print("Finalizando o programa. Até logo!")
            break   
        else:
            print("Opção inválida. Por favor, tente novamente.")