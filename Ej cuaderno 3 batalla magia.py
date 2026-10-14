from random import randint
vida_jugador = 100
vida_IA = 200
combate = 0
rondas = 0
print("¡Te estan atacando! Presion 1 para ataque básico, 2 para congelar, 3 para quemar, 4 para hechizo de curación, 5 para escudo")
while combate==0:
    ataque_IA = randint(10, 25)
    vida_jugador = vida_jugador - ataque_IA
    rondas =rondas+1
    print("ronda:" ,rondas)
    decisión=input("¿Que harás?")
    if decisión == "1":
        contrataque=randint(10, 25)
        vida_IA = vida_IA - contrataque
    elif decisión == "5":
        vida_jugador = vida_jugador + (ataque_IA/4*3)
    elif decisión == "4":
        curación=randint(10, 40)
        vida_jugador == vida_jugador + curación
        if vida_jugador > 100:
         vida_jugador == 100
    else:
        print("esa no es una opción, tu enemigo te ha restado vida")
    print("Tu vida:" ,vida_jugador)
    print("Vida del rival", vida_IA)
    if vida_IA <= 0 and vida_jugador <= 0:
        print("Empate, ambos murieron")
        print("el combate ha durado", rondas, " rondas")
        combate=1
    elif vida_jugador <= 0:
        print("PERDISTE")
        print("el combate ha durado", rondas, " rondas")
        combate=1
    elif vida_IA <= 0:
        print("¡GANASTE!")
        print("el combate ha durado", rondas, " rondas")
        combate=1