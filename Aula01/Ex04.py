start_campos = True
start_programa = True
campo = 1

while start_programa:
    while start_campos:
        
        match campo:
            case 1:
                try:
                    nome = input("Digite seu nome:")
                    campo += 1
                except:
                    print("Nome inválido")
            case 2:
                try:
                    idade = int(input("Digite sua idade:"))
                    campo += 1
                except:
                    print("Nome inválido")
            case 3:
                try:
                    peso = float(input("Digite seu peso em kilos:").replace(",", "."))
                    campo += 1
                except:
                    print("Nome inválido")
            case 4:
                try:
                    altura = float(input("Digite sua altura em metros: ").replace(",", "."))
                    start_campos = False
                except:
                    print("Nome inválido")
    else:
        
                
    
        imc = peso / (altura ** 2)
        print("Nome:", nome)
        print("Idade:", idade)
        print("%.2f" % round(imc, 2))

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 24.9:
            print("Classificação: Peso normal")
        elif 25 <= imc < 29.9:
            print("Classificação: Sobrepeso")
        elif 30 <= imc < 39.9:
            print("Classificação: Obesidade")
        else: 
            print("Classificação: Obesidade morbida")

        fim_programa = True
        while fim_programa:
            print("\nDeseja finalizar o programa?\n")
            try:
                confirma = str(input("Digite S (SIM) ou N (Não Finalizar): "))
                if confirma == "S" or confirma == "s":
                    fim_programa = False
                    start_programa = False
                elif confirma == "n" or confirma == "N":
                    fim_programa = False
                    start_campos = True
                    campo = 1
                    
                else:
                    print("Valor inválido")
            except:
                print("Campo invalido")
else:
    
    pass
    
print("\n Programa finalizado \n")
    
