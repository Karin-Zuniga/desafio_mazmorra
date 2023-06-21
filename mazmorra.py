
#var_1 = nombre_juego
#var_2 = jugador
#var_3 = nivel ==> 3 niveles
#F(x) 1 = historia



def nivel_1():
    pass

def nivel_2():
    pass

def nivel_3():
    pass








def main():
    nombre_juego = "Escape de la mazmorra"

    jugador = input(f"Bienvenido a {nombre_juego}\nCual es tu nombre?\n")
    nivel = input(f"Bienvenido {jugador}\nEn que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1.Facil\n2. Medio\n3. Dificil\n")

    if nivel == "1" or nivel == "2" or nivel == "3":
        historia()
        print("Caminas por un bosque en medio de la noche. De repente, tus pies pisan una puerta. Por curiosidad, la abres y ves una escalera colgante, por lo que decides ir a investigar...\n...bajas lo que parecen ser tres pisos, y tan pronto como tus pies tocan el suelo, la puerta se cierra y la escalera cae.\n ...Parece ser que estas en un grave problema...")
    else:
        print("Opcion no valida. Adios")


main()