from traceback import print_stack
class Usuario():
    def __init__(self, login, password):
        self._login=login
        self._password=password
        self.register()

    def register(self):
        arquivo = open("user.txt","a")
        user=self._login    
        registrar=True

        with open('user.txt') as f:
            file=f.readlines()

        for line in file:
            if line.strip().split(" ")[0] == user: #pega so o usuario da linha
                print ("Usuario ja foi criado")
                registrar=False
                break
    

        
        if registrar :
            password=self._password 
            arquivo.write(user+" "+password+"\n") 
            print("registrando")     
        arquivo.close()

