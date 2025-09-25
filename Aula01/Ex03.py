def calculadora():
    """
    Calculadora simples com as 4 operações básicas.
    """
    while True:
        print("\n=== CALCULADORA SIMPLES ===")
        print("1. Soma (+)          2. Subtração (-)")
        print("3. Multiplicação (*) 4. Divisão (/)")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == '5':
            print("Obrigado por usar a calculadora! Saindo...")
            break
        
        if opcao not in ['1', '2', '3', '4']:
            print("❌ Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")
            continue
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                resultado = num1 + num2
                print(f"📊 Resultado: {num1} + {num2} = {resultado}")
            elif opcao == '2':
                resultado = num1 - num2
                print(f"📊 Resultado: {num1} - {num2} = {resultado}")
            elif opcao == '3':
                resultado = num1 * num2
                print(f"📊 Resultado: {num1} * {num2} = {resultado}")
            elif opcao == '4':
                if num2 == 0:
                    print("❌ Erro: Divisão por zero não é permitida!")
                else:
                    resultado = num1 / num2
                    print(f"📊 Resultado: {num1} / {num2} = {resultado}")
                    
        except ValueError:
            print("❌ Erro: Digite apenas números válidos (ex.: 5, 3.14)!")
        
        # Pausa para o usuário ver o resultado
        input("\nPressione Enter para continuar...")
# Executa a calculadora se o script for rodado diretamente
if __name__ == "__main__":
    calculadora()
