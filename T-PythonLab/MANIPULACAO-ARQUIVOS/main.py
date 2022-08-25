
arquivo = open("data/sitemas.txt","a")
continuar=True
while continuar:
    os_name = input ("Digite um OS (vazio para sair):")
    if not os_name:
        continuar=False
        continue
    arquivo.write(os_name+"\n")
arquivo.close()