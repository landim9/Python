import login
import menu_principal
import letreiro
import config

print("Seja bem vindo ao sistema\n")
print(letreiro.banner_pagga("COTA-FRETE"))
acesso = login.main()
if acesso:
    menu_principal.main()
    config.limpa_tela()

print("\n<<<<<<<< Obrigado por utilizar o sistema COTAFRETE!")