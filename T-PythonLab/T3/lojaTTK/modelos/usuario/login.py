

def login(user,password):


    file=open("user.txt")

    with open('user.txt') as f:
        file=f.readlines()

    for line in file:
        if line.strip().split(" ")[0] == user and line.strip().split(" ")[1] == password:
            return user

    print("usuario ou senha errado")
    return 0