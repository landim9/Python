pi = 3.14159
while True:
    
    while True:
        try:
            raio = float(input("Digite o raio da circunferência: ").strip().replace(",", "."))
            break
        except ValueError:
            print("Raio inválido! Deve ser um número (use . ou ,).")
    
    c = raio / (2 * pi)
    print(f"A circunferência é: {c:.2f}")
    
    while True:
        print("\nDeseja finalizar o programa?")
        try:
            confirma = input("Digite S (SIM) ou N (Não Finalizar): ").strip().upper()
            if confirma == "S":
                print("\nPrograma finalizado\n")
                exit() 
            elif confirma == "N":
                break  
            else:
                print("Valor inválido! Digite S ou N.")
        except ValueError:
            print("Entrada inválida!")