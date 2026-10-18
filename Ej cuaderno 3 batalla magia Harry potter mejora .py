from random import randint
vida_jugador =float(100)
vida_IA = 200
combate = 0
rondas = 0
intentos_Petrificus_Totalus = 3
Petrificus_Totalus = 0
intentos_fuego = 3
expelliarmus = 0
probabilidad_ataquea_especial_IA = 0
inmovilizado = False
print("¡Te estan atacando! Presion 1 para ataque básico, 2 para Petrificus Totalus, 3 para quemar, 4 para poción de díctamo, 5 para escudo")
while combate==0:
    ataque_IA = randint(10, 30)
    vida_jugador = vida_jugador - ataque_IA
    print("ronda:" ,rondas)
    decisión=input("¿Que harás?")
    if decisión == "1":
        contrataque=randint(10, 25)
        vida_IA = vida_IA - contrataque
    elif decisión =="2":
        if intentos_Petrificus_Totalus>0:
         Petrificus_Totalus=2
         vida_IA = vida_IA - 5
         intentos_Petrificus_Totalus = intentos_Petrificus_Totalus - 1
         inmovilizado = True
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
         vida_jugador = 100
    elif decisión == "5":
        if inmovilizado == False:
         vida_jugador = vida_jugador + (ataque_IA/4*3)
    elif decisión == "expelliarmus":
        expelliarmus=3
        inmovilizado = True
    elif decisión == "avada kedavra":
      vida_IA = 0
    elif decisión == "confringo":
        vida_IA = vida_IA - 45
        chance_daños = randint(1,5)
        if chance_daños == 5:
            vida_jugador =  vida_jugador-5
    else:
        print("esa no es una opción, tu enemigo te ha restado vida")
    if Petrificus_Totalus>0:
        vida_jugador=vida_jugador+ataque_IA
        Petrificus_Totalus = Petrificus_Totalus - 1
    if expelliarmus>0:
        vida_jugador=vida_jugador+ataque_IA
        expelliarmus = expelliarmus - 1
    probabilidad_ataquea_especial_IA =int(randint(1,10)) 
    if probabilidad_ataquea_especial_IA == 7:
        if decisión == "expelliarmus":
            print("prior incantamem")
            vida_IA = 0
        elif inmovilizado == False:
            vida_jugador = vida_jugador - vida_jugador
            print("te han asesinado con avada kedavra")
    if probabilidad_ataquea_especial_IA == 3:
        if inmovilizado == False:
            print("Oh no, te han atacado con crucio.") 
            vida_jugador = vida_jugador- 20
            rondas = rondas + 1
            print(vida_jugador)
            print("rondas:", rondas)
            vida_jugador = vida_jugador- 20
            rondas = rondas + 1
            print(vida_jugador)
            print("rondas:", rondas)
    rondas =rondas+1
    print("Tu vida:" ,vida_jugador)
    print("Vida del rival", vida_IA)
    if vida_jugador < 0:
        vida_jugador = 0
    if vida_IA < 0:
        vida_IA = 0
    if vida_IA == 0 and vida_jugador == 0:
        print("Empate, ambos murieron")
        print("el combate ha durado", rondas, " rondas")
        combate=1
    elif vida_jugador == 0:
        print("PERDISTE")
        print("el combate ha durado", rondas, " rondas")
        combate=1
    elif vida_IA == 0:
        print("¡GANASTE!")
        print("el combate ha durado", rondas, " rondas")
        combate=1