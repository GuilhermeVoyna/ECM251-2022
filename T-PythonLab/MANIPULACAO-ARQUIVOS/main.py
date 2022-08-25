from traceback import print_stack

#Codigo de ler arquivo  (// > . < //)
 
try:
    arquivo = open("data/sitemas.txt","a")
    continuar=True
    while continuar:
        os_name = input ("Digite um OS (vazio para sair):")
        if not os_name:
            continuar=False
            continue
        arquivo.write(os_name+"\n")
    arquivo.close()
except FileNotFoundError:
    print("Caminho não exixte, favor verificar")
except Exception:
    print("Algo não experado ocorreu:")
    print_stack()
finally:
    print("Chegamos no final")
