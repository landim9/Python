# a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e peso e ao final deverá mostrar todos os dados de forma personalizada;
# Entrada de dados
nome = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: "))
peso = input("Digite seu peso: ")

# Saída personalizada
print("\n------------------------------------------")
print("Nome:", nome)
print("Idade:", idade, "anos")

if idade < 12:
    print("Criança")
elif 12 <= idade < 17:
    print("Adolescente")
else: 
    print("Adulto")
    
print("Peso:", peso, "kg")
print("------------------------------------------")
