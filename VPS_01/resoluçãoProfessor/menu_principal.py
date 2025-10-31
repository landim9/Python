import mod_inputs
import calculadora
import config
import letreiro

def menu():
    print(letreiro.banner_pagga("MENU PRINCIPAL"))
    print("\nEscolha um programa: ")
    print("Sair => 0 |  Calculadora => 1 | Cota Frete => 2")

def recebe_menu():
    num = mod_inputs.inp_int("Informe o programa que deseja acessar: ")
    return num

def valida_menu(num):
    programa = True
    match num:
        case 0:
            programa = False
        case 1:
            calculadora.main()
        case 2:
            print("Chamar o Cota-Frete")
        case _:
            print("Menu inválido...")
    return programa

def main():
    config.limpa_tela()
    executa = True
    while executa:
        menu()
        num = recebe_menu()
        executa = valida_menu(num)
    return executa

if __name__ == "__main__":
    main()
