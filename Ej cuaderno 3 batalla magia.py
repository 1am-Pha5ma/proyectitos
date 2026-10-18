from random import randint
vida_jugador = 100
vida_IA = 200
combate = 0
rondas = 0
intentos_hielo = 3
hielo = 0
intentos_fuego = 3
print("¡Te estan atacando! Presion 1 para ataque básico, 2 para congelar, 3 para quemar, 4 para hechizo de curación, 5 para escudo")
while combate==0:
    ataque_IA = randint(10, 30)
    vida_jugador = vida_jugador - ataque_IA
    rondas =rondas+1
    print("ronda:" ,rondas)
    decisión=input("¿Que harás?")
    if decisión == "1":
        contrataque=randint(10, 25)
        vida_IA = vida_IA - contrataque
    elif decisión =="2":
        if intentos_hielo>0:
         hielo=2
         vida_IA = vida_IA - 5
         intentos_hielo = intentos_hielo - 1
         vida_jugador = vida_jugador - ataque_IA
        else:
            print("Ya agotaste ese hechizo")
    elif decisión =="3":
        if intentos_fuego>0:
         vida_IA = vida_IA - 50
         vida_jugador = vida_jugador - 5
        else:
            print("Ya agotaste ese hechizo")
    elif decisión == "4":
        curación=randint(20, 40)
        vida_jugador = vida_jugador + curación
        if vida_jugador > 100:
         vida_jugador == 100
    elif decisión == "5":
        vida_jugador = vida_jugador + (ataque_IA/4*3)
    else:
        print("esa no es una opción, tu enemigo te ha restado vida")
    if hielo>0:
        vida_jugador=vida_jugador+ataque_IA
        hielo = hielo - 1
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