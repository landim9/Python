# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso e ao final deverá mostrar todos os dados de forma personalizada;
# Entrada de dados

start_campos = True
campo = 1

while start_campos:

    match campo:
        case 1:
            try:
                nome = str(input("Digite seu nome completo: "))
                campo += 1
            except:
                print("Nome inválido")
        case 2:  
            try:
                idade = int(input("Digite sua idade em anos: "))
                campo += 1
            except:
                print("Idade inválida!") 
                
        case 3:
            try:
                peso = float(input("Digite seu peso em Kg: "))
                start_campos = False
            except:
                print("Peso inválido!")
else:
# Saída personalizada
    print("\n------------------------------------------")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Peso:", peso, "Kgs")
    print("------------------------------------------\n")


