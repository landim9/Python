def obter_nome():
    while True:
        try:
            nome = input("Digite seu nome completo: ").strip()
            if nome:  # Verifica se não está vazio
                return nome
            else:
                print("Nome inválido! Digite um nome não vazio.")
        except:
            print("Nome inválido!")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade em anos: ").strip())
            if idade > 0:  # Idade deve ser positiva
                return idade
            else:
                print("Idade inválida! Digite um número positivo.")
        except ValueError:
            print("Idade inválida! Digite um número inteiro válido.")
        except:
            print("Idade inválida!")

def obter_peso():
    while True:
        try:
            peso_input = input("Digite seu peso em Kg: ").strip().replace(",", ".")
            peso = float(peso_input)
            if peso > 0:  # Peso deve ser positivo
                return peso
            else:
                print("Peso inválido! Digite um número positivo.")
        except ValueError:
            print("Peso inválido! Digite um número decimal válido (use ponto para decimais).")
        except:
            print("Peso inválido!")

def mostrar_dados(nome, idade, peso):
    print("\n------------------------------------------")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Peso:", peso, "Kgs")
    print("------------------------------------------\n")

def confirmar_finalizacao():
    while True:
        try:
            confirma = input("Deseja finalizar o programa?\nDigite S (SIM) ou N (Não Finalizar): ").strip().upper()
            if confirma == "S":
                return True
            elif confirma == "N":
                return False
            else:
                print("Valor inválido! Digite S ou N.")
        except:
            print("Campo inválido! Digite S ou N.")

if __name__ == "__main__":
    start_programa = True
    
    while start_programa:
        nome = obter_nome()
        idade = obter_idade()
        peso = obter_peso()
        
        mostrar_dados(nome, idade, peso)
        
        if confirmar_finalizacao():
            start_programa = False
    
    print("\nPrograma finalizado\n")