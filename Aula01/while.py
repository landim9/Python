inicio = True

contador = 0

while contador < 10:
    contador += 1
    print("Executando código", contador)

else:
    print("Laço encerrado")
    
contador2 = 3

match contador2:
    case 1:
        print("Executa caso seja: ", contador2)
    case 2:
        print("Executa caso seja: ", contador2)
    case 3:
        print("Executa caso seja: ", contador2)