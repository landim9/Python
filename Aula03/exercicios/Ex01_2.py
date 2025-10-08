def receber_dados():
    campo = 1
    while True:
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
                    campo += 1 
                    return False
                except:
                    print("Peso inválido!")

def mostrar_dados():
    print("Seu nome é:", nome) # type: ignore
    print("Seu peso é: ", peso, "Kgs") # type: ignore #
    print("Sua idade é: ", idade, "anos") # type: ignore #


if __name__ == "__main__":
    
    start_programa = True
    
    while start_programa:
        receber_dados(nome, idade, peso) # type:ignore 
        
        mostrar_dados(nome, idade, peso) #type:ignore
        
        if confirmar_finalizacao(): #type:ignore
            start_programa = False
    
    print("\nPrograma finalizado\n")