from traceback import print_stack

#Codigo de ler arquivo  (// > . < //)
 
with open('login.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
