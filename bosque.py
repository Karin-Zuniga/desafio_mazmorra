import time
import random

def transformar_a_numero(respuesta):
    try:
            respuesta = float(respuesta)
            return respuesta
    except ValueError:
        salir = input("valor no valido, deseas salir(si/no)\n")
        if salir == "si":
            final = True
            return final


def primera_pregunta(nivel, diario, msg_diario):
    valor_respuesta = False
    patron_usuario = ""

    advertencia = "Vas por mal camino, sigue asi y te quedaras dentro.\n"
    felicidades = "Sigue asi y puede que logres salir\n"

    while valor_respuesta == False:
        respuesta = input("Cual es el resultado del seno(30)+cos(60)?\n")
        
        final = transformar_a_numero(respuesta)
        
        if final == True and isinstance(final, str) == True:
            return final
        elif final != 1 and isinstance(final, str) == False:
            print(advertencia)
        
        elif final == 1:
            print(felicidades)
            valor_respuesta = True

        else:
            print("algo salio mal")

    patron = [1,2,3,4]
    print("************") 
    for numero in patron:
        numero = str(numero)
        print(numero, end="")
        patron_usuario = patron_usuario + numero

    print("\n************") 
    

    valor = input(f"Deseas agregar {patron_usuario} a tu diario (si/no)?\n")
    valor = valor.lower()
    if valor == "si":
        diario.append(patron_usuario)
        valor = input(msg_diario)
        if valor.lower() == "si":
            print(diario)







def main():
    nombre_juego = "Escape del bosque"
    inicio = "Estas atrapado dentro del bosque. Para salir deberas resolver 6 acertijos matematicos. Al final de cada ejercicio se te dara un numero. Encuentra el patron para salir o si no, te quedaras atrapado en un bucle para siempre, suerte :)\n" 
    msg_diario = "Deseas revisar tu diario?\n"

    final = False
    diario = []
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
            final = primera_pregunta(nivel, diario, msg_diario)
            print("Gracias por jugar")


       


    

main()