import time
import random

def definir_patron(nivel):
    patron = [] 
    patron_usuario = ""
    a = random.randint(1,25)
    b = random.randint(1,25)

    patron = [a, b]

    if nivel == "1":
         for i in range(0,4):
            c = patron[-2] - patron[-1]
        
            int(c)
            patron.append(c)
    elif nivel == "2":

        for i in range(0,4):
            if patron[-2] % patron[-1] == 0:
                c = patron[-2] + patron[-1]
            else:
                c = patron[-2] - patron[-1]
            int(c)
            patron.append(c)
                    
    print("************") 
    for numero in patron:
        numero = str(numero)
        print(numero, end=" ")
        patron_usuario = patron_usuario + " " + numero

    print("\n************") 
    
    return patron_usuario


def transformar_a_numero(respuesta):
    if respuesta == "salir":
        print("************************")
        final = True
        return final
    else:
        try:
            respuesta = float(respuesta)
            return respuesta
        except ValueError:       
            print("valor no valido")

def agregar_a_diario(patron_usuario, diario, msg_diario):
    valor = input(f"Deseas agregar {patron_usuario} a tu diario (si/no)?\n")
    valor = valor.lower()
    if valor == "si":
        diario += [patron_usuario]
        valor = input(msg_diario)
        if valor.lower() == "si":
            return diario
    




def primera_pregunta(nivel, diario, msg_diario):
    valor_respuesta = False
    advertencia = "No, me temo que no"
    felicidades = "Buena suerte en la siguiente... la necesitaras"

    while valor_respuesta == False:
        msg_facil = "PASO  es a APSO como 3240 es a...?\n"
        msg_dificil ="Cual...\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 2340 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 2340 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True


        elif  nivel == "2" and final != 1 and isinstance(final, float) == True:
            print(advertencia)
        
        elif nivel == "2" and final == 1 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True
        


    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario, msg_diario)
    
    final = False

    return final, diario


def segunda_pregunta(nivel, diario, msg_diario):
    valor_respuesta = False
    

    advertencia = "Vas por mal camino, sigue asi y te quedaras dentro.\n"
    felicidades = "Sigue asi y puede que logres salir\n"

    while valor_respuesta == False:
        msg_facil = "Si la mitad de 6.446 es 3.223 y la mitad de 6.612 es 3306, cuanto es la mitad de 88.442.288?(escribe la respuesta sin puntos)\n"
        msg_dificil ="Cual es el resultado del seno(30)+cos(60)?\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 44221144 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 44221144 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True


        elif final != 1 and isinstance(final, float) == True and nivel == "2":
            print(advertencia)
        
        elif final == 1 and nivel == "2" and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        else:
            print("algo salio mal")

    patron_usuario = definir_patron(nivel)
    
    diario = agregar_a_diario(patron_usuario, diario, msg_diario)
    
    final = False

    return final, diario







def main():
    nombre_juego = "Escape del bosque"
    inicio = "Estas atrapado dentro del bosque. Para salir deberas resolver 6 acertijos matematicos. Al final de cada ejercicio se te dara un conjunto de numeros. Encuentra la regla del patron para abrir la puerta final, o sino, te quedaras atrapado en un bucle para siempre, suerte :)\n" 
    msg_diario = "Deseas revisar tu diario?\n"

    final = False
    diario = []
    print(f"Bienvenido a {nombre_juego}\n")
    
    time.sleep(0.5)
    
    jugador = input(f"Cual es tu nombre?\n")
    
    time.sleep(0.5)
    
    print(f"Hola {jugador}")
    

    time.sleep(1)
    
    nivel = input("En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1. Facil\n2. Dificil\n")
    
    if nivel == "1" or nivel == "2":
        time.sleep(0.5)
        while final == False:
            print(inicio)
            final, diario = primera_pregunta(nivel, diario, msg_diario)
            final, diario = segunda_pregunta(nivel, diario, msg_diario)
            
            print("Gracias por jugar")





            respuesta = input("Deseas otra partida?(si/no)")
            if respuesta == "no":
                final = True
            else:
                final = False




       


    

main()