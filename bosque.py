import time
import random
def primera_pregunta(nivel):
    valor_respuesta = False

    advertencia = "Vas por mal camino, sigue asi y te quedaras dentro."
    felicidades = "Sigue asi y puede que logres salir"


    while valor_respuesta == False:
        respuesta = input("Cual es el resultado del seno(30)+cos(60)?\n")
        try:
            respuesta = int(respuesta)
        except ValueError:
            salir = input("valor no valido, deseas salir(si/no)")
            if salir == "si":
                final = True
                return final
           
        if respuesta != 1:
            print(advertencia)
        
        else:
            print(felicidades)
            valor_respuesta = True





def main():
    nombre_juego = "Escape del bosque"
    inicio = "Estas atrapado dentro del bosque. Para salir deberas resolver 6 acertijos e ingresarlos en la ultima pregunta si quieres vivir. Si no, te quedaras atrapado en un bucle para siempre, suerte :)" 
    final = False
    
    print(f"Bienvenido a {nombre_juego}\n")
    
    time.sleep(0.5)
    
    jugador = input(f"Cual es tu nombre?\n")
    
    time.sleep(0.5)
    
    print(f"Hola {jugador}")
    
    time.sleep(1)
    
    nivel = input("En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1.Facil\n2. Medio\n3. Dificil\n")
    
    if nivel == "1" or nivel == "2" or nivel == "3":
        time.sleep(0.5)
        while final == False:
            print(inicio)
            final = primera_pregunta(nivel)
            print("Gracias por jugar")


       


    

main()