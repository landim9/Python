def pegar_nome():
    while True:
        try:
            nome = input("Digite seu nome completo: ").strip()
        except:
            print("Valor invalido")

def pegar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade em anos: ").strip())
        except:
            print("Valor invalido")

def pegar_peso():
    while True:
        try:
            peso = print(float(input("Digite seu peso: ")))
        except:
            print("Valor invalido")

def mostra_dados(nome, idade, peso):

    print("\n------------------------------------------")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Peso:", peso, "Kgs")
    print("------------------------------------------\n")

def finalizar():

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

    nome = pegar_nome()
    idade = pegar_idade()
    peso = pegar_peso()


    mostra = mostra_dados(nome, idade, peso)

    if finalizar():
        start_programa = False
    # Se não finalizar, o loop reinicia e coleta novos dados

print("\nPrograma finalizado\n")
