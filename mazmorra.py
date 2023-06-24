
#var_1 = nombre_juego
#var_2 = jugador
#var_3 = nivel ==> 3 niveles
#F(x) 1 = historia
#Alguna forma de evitar el error por ingreso de datos invalidos?
import time
import random

def historia(nivel,final):

    puerta_primer_piso = str(input("Alrededor tuyo hay 4 puertas. \n Que puerta eligiras?\n1. Puerta Sur\n2. Puerta Norte\n3. Puerta Este\n4. Puerta Oeste\n"))
    if puerta_primer_piso == "1":
        habitacion_1_a(nivel)
    elif puerta_primer_piso == "2":
        habitacion_1_b(nivel)
    elif puerta_primer_piso == "3":
        habitacion_1_c(nivel)
    elif puerta_primer_piso == "4":
        habitacion_1_d(nivel)
    elif puerta_primer_piso.lower() == "salir":
        print("adios")
        final = True
    else:
        print("opcion no valida. Para salir ingresa 'salir'")





def puertas(numero_puertas):
    if numero_puertas > 2:
        norte = "3. Norte\n"
        direccion = " al norte,"
    else:
        norte = ""
        direccion = ""
    puerta = input(f"Tienes {numero_puertas} puertas que dan{direccion} al este, y al oeste.\nHacia cual correras?\n1. Este\n2. Oeste\n{norte}")
    return puerta 

def tirar_piedras(cantidad):
    piedras_totales = 0
    for i in range(0,11):
        piedras_derecha = random.randint (0,cantidad)
        piedras_izquierda = random.randint (0,cantidad)
        piedras = int(input(f"Por la derecha vienen {piedras_derecha} y por la izquierda {piedras_izquierda}\nCuantas vienen?\n"))
        suma_piedras = piedras_derecha + piedras_izquierda    
        if piedras != suma_piedras:
            print("Ouch! Eso debio doler.")
        elif suma_piedras == piedras_totales:
            piedras_totales =  piedras_totales + 1
        else:
            print("para salir ingresa '0'")

    if piedras_totales >= 8:
        print("Felicidades! Haz logrado llegar a la puerta.")
    else:
        print("Estas muy malherido para continuar. Mejor suerta para la proxima")

def habitacion_1_a(nivel):
    print("Te encuentras en una habitacion con muros de piedra.")
    puerta = puertas(2)
    print("Corres lo mas rapido que puedes pero en mitad del camino pisas una trampa y una maquina en cada lado de la habitacion empieza a tirar piedras hacia ti. Mejor las cuentas las piedras para asegurarte que las esquivaste todas.")
    if nivel == "1":
        tirar_piedras(16)
            

    elif nivel == "2":
        tirar_piedras(50)
    elif nivel == "3":
        tirar_piedras(150)
    else:
        print("Algo no funciono")
    

def habitacion_1_b(final):
    pass

def habitacion_1_c(final):
    pass

def habitacion_1_d(final):
    pass

def habitacion_2_a(final):
    pass

def habitacion_2_b(final):
    pass

def habitacion_2_c(final):
    pass

def habitacion_2_d(final):
    pass   

def habitacion_2_e(final):
    pass

def habitacion_2_f(final):
    pass

def habitacion_2_g(final):
    pass

def habitacion_2_h(final):
    pass

def habitacion_3_a(final):
    pass

def habitacion_3_b(final):
    pass

def habitacion_3_c(final):
    pass

def habitacion_3_d(final):
    pass

def habitacion_3_e(final):
    pass

def habitacion_3_f(final):
    pass

def habitacion_3_g(final):
    pass

def habitacion_3_h(final):
    troll = int(input("Tropiezas y caes al suelo, al levantar la cabeza 30 grados, ves que hay un troll de dos metros frente a ti. Calcula la distancia a la cual esta el troll, para saber si alcanzas a huir."))
    if troll > 4:
        print("Oh no, haz sobreestimado la distancia. El troll corre hacia ti y te alcanza.\nMejor suerte la proxima vez ")
        final = True
    elif troll > 3 and troll < 4:
     #correcto
        pass

    elif troll < 3:
        print("Oh no, haz subestimado la distancia y perdiste tu oportunidad de escapar. De haber corrido mas lejos, podrias haber cruzado la puerta siguiente. Lo siento, haz perdido.")


    elif troll.lower() == "salir":
        print("adios")
        final = True
    else:
        print("opcion no valida. Para salir ingresa 'salir'")        



def main():
    nombre_juego = "Escape de la mazmorra"
    final = False
    print(f"Bienvenido a {nombre_juego}\n")
    time.sleep(1)
    jugador = input(f"Cual es tu nombre?\n")
    time.sleep(1)
    print(f"Hola {jugador}")
    time.sleep(1)
    nivel = input(f"En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1.Facil\n2. Medio\n3. Dificil\n")

    if nivel == "1" or nivel == "2" or nivel == "3":
        time.sleep(2)
        print("Caminas por un bosque en medio de la noche. De repente, tus pies pisan una puerta. Por curiosidad, la abres y ves una escalera colgante, por lo que decides ir a investigar...\n...bajas lo que parecen ser tres pisos, y tan pronto como tus pies tocan el suelo, la puerta se cierra y la escalera cae.\n ...Parece ser que estas en un grave problema...")
    while final == False:
        historia(nivel, final)
        
    else:
        print("Opcion no valida. Adios")


main()