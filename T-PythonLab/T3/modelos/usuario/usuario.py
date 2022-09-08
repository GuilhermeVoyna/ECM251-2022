class Usuario():
    def __init__(self, login, password):
        self._login=login
        self._password=password
        self.register()

    def register(self):
        file=open("user.txt","a")
        file.write("\n" + self._login + " "+ self._password)
        file.close()
