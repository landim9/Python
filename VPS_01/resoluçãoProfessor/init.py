import login
import menu_principal

print("\nSeja bem vindo ao sistema COTA FRETE")
acesso = login.main()
if acesso:
    menu_principal.main()

print("\n<<<<<<<< Obrigado por utilizar o sistema COTAFRETE!")