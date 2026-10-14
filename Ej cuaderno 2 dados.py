from random import choice
dados=[1, 2, 3, 4, 5, 6]
rondas=1
puntos1=0
puntos2=0
while rondas<=5:
    print("Ronda:", rondas)
    rondas+1
    input("presiona ENTER para tirar los dados")
    dado1 = choice(dados)
    dado2 = choice(dados)
    print("tu dado:" ,dado1)
    print("el otro dado:" ,dado2)
    if dado1 > dado2:
        print("Ganaste")
        puntos1+1
    elif dado1 < dado2:
        print("Perdiste")
        puntos2+1
    else:
        print("Empate")
    rondas+1
if puntos1 > puntos2:
    print("Ganaste el duelo")
elif puntos1 <puntos2:
    print("Perdiste el duelo")
else:
    print("Empate")
    
