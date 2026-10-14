N=input ("ingrese su contraseña")
intentos=0
C=12345
while (int(intentos)<=5) or N==C:
    intentos=intentos+1
    if (int(N)==12345):
        print ("acceso concedido")
    else:
     print ("NO")
if intentos>5:
    print("Lo lamento, agoto sus intentos") 