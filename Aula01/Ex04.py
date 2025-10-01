nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura: (Ex: 1.75)"))

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

        
   