nome = input("Digite seu nome:")
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura: (Ex: 1.75)"))

imc = peso / (altura ** 2)

print("%.2f" % round(imc, 2))

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 39.9:
    print("Obesidade")
else: 
    print("Obesidade morbida")