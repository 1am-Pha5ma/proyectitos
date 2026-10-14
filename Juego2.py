from random import randint
N= randint(0, 100) 
I=0
M=input("ingresa un número del 1 al 100")
while (int(I)==4) or int(M)==N:
     I=I+1
     M=input ("ingresa otro número del 1 al 100")
     if (int(M)<N):
         print ("Un poco más alto, no seas avaro")
     else:
          print ("Epa exagerado, no tanto")
if M==N:
    print ("muy bien adivinaste")
else:
    if I==4:
        print("Alpiste perdiste")