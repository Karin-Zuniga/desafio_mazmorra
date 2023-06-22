
#var_1 = nombre_juego
#var_2 = jugador
#var_3 = nivel ==> 3 niveles
#F(x) 1 = historia


def habitacion_1_a(final):
    pass    

def habitacion_1_a(final):
    pass

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

def historia():
    final = False
    while final == False:
        puerta_primer_piso = input("Alrededor tuyo hay 4 puertas. \n Que puerta elijiras?\n1. Puerta Sur\n2. Puerta Norte\n3. Puerta Este\n4. Puerta Oeste\n")
        if puerta_primer_piso == "1":
            habitacion_1_a(final)
        elif puerta_primer_piso == "2":
            habitacion_1_b(final)
        elif puerta_primer_piso == "3":
            habitacion_1_c(final)
        elif puerta_primer_piso == "4":
            habitacion_1_d(final)
        elif puerta_primer_piso.lower(final) == "salir":
            print("adios")
            final = True
        else:
            print("opcion no valida. Para salir ingresa 'salir'")



def main():
    nombre_juego = "Escape de la mazmorra"
    print(f"Bienvenido a {nombre_juego}\n")
    jugador = input(f"Cual es tu nombre?\n")
    
    #preguntar si se pueden usar librerias... 
    #import time
    #time.sleep()
    print(f"Hola {jugador}")
    #time.sleep(1)
    nivel = input(f"En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1.Facil\n2. Medio\n3. Dificil\n")

    if nivel == "1" or nivel == "2" or nivel == "3":
        #time.sleep()
        print("Caminas por un bosque en medio de la noche. De repente, tus pies pisan una puerta. Por curiosidad, la abres y ves una escalera colgante, por lo que decides ir a investigar...\n...bajas lo que parecen ser tres pisos, y tan pronto como tus pies tocan el suelo, la puerta se cierra y la escalera cae.\n ...Parece ser que estas en un grave problema...")
        historia()
        
    else:
        print("Opcion no valida. Adios")


main()