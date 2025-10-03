# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso e ao final deverá mostrar todos os dados de forma personalizada;
# Entrada de dados

start_campos = True
campo = 1
start_programa = True

while start_programa:
    while start_campos:

        match campo:
            case 1:
                try:
                    nome = (input("Digite seu nome completo: ").strip)
                    campo += 1
                except:
                    print("Nome inválido")
            case 2:  
                try:
                    idade = int(input("Digite sua idade em anos: ").strip)
                    campo += 1
                except:
                    print("Idade inválida!") 
                    
            case 3:
                try:
                    peso = float(input("Digite seu peso em Kg: ").strip .replace(",", "."))
                    start_campos = False
                except:
                    print("Peso inválido!")
    else:
        print("\n------------------------------------------")
        print("Nome:", nome)
        print("Idade:", idade, "anos")
        print("Peso:", peso, "Kgs")
        print("------------------------------------------\n")
        
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
    


