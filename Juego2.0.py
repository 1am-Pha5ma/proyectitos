from random import randint
N= randint (0, 10)
Gane=False
while Gane==False:
    M=input ("escriba un número entre 1 y 10: ")
    if (int(M)==N):
        print ("Ganaste!!!!!")
        Gane=True
    else:
        if (int(M)>N):
            print ("Tu numero es mas grande que el mio")
        else:
            print ("Tu numero es mas chico que el mio")
