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

def transformar_a_numero(respuesta, advertencia):

    if respuesta == "salir":
        final = True
        return final
    else:
        try:
            respuesta = float(respuesta)
            if respuesta == 1:
                print(advertencia)
            else:
                return respuesta
        except ValueError:       
            print("valor no valido")

def agregar_a_diario(patron_usuario, diario):
    msg_diario = "Deseas revisar tu diario?\n"
    terminar = False
    while terminar == False:
        valor = input(f"Deseas agregar {patron_usuario} a tu diario (si/no)?\n")
        valor = valor.lower()
        if valor == "si":
            diario += [patron_usuario]
            valor = input(msg_diario)
            if valor.lower() == "si":
                print(diario)
                return diario
            elif valor.lower() == "no":
                return diario
            else:
                continue
        elif valor == "no":
            return diario
    
def primera_pregunta(nivel, diario):
    
    valor_respuesta = False
    advertencia = "No, me temo que no"
    felicidades = "Buena suerte en la siguiente... la necesitaras"

    while valor_respuesta == False:
        msg_facil = "PASO  es a APSO como 3240 es a...?\n"
        msg_dificil ="Una familia de dos padres, tres hijos (todos niños), y el abuelo comen tres pizzas. Cada adulto come tres piezas, y los niños comen una, pero le piden a sus padres otra pieza que solo la mazcan y devuelven. Cuantos trozos enteros de pizza quedan si la pizza esta cortada en ocho piezas? \n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 2340 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 2340 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 3 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 3 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def segunda_pregunta(nivel, diario):
    valor_respuesta = False
    advertencia = "Vas por mal camino, sigue asi y te quedaras dentro.\n"
    felicidades = "Sigue asi y puede que logres salir\n"

    while valor_respuesta == False:
        msg_facil = "Si la mitad de 6.446 es 3.223 y la mitad de 6.612 es 3306, cuanto es la mitad de 88.442.288?(escribe la respuesta sin puntos)\n"
        msg_dificil ="Los minutos en dos horas y cuarto, dividos en tres son:\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
                
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 44221144 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 44221144 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True


        elif nivel == "2" and final != 45 and isinstance(final, float) == True:
            print(advertencia)
        
        elif nivel == "2" and final == 45 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        else:
            print("algo salio mal")

    patron_usuario = definir_patron(nivel)
    
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def tercera_pregunta(nivel, diario):
    valor_respuesta = False
    advertencia = "Lamento decirlo, pero estas equivocado."
    felicidades = "Lo haz hecho bien, supongo."

    while valor_respuesta == False:
        msg_facil = "Si tengo 22 años, en 27 años tendre 49. Si pasan 16 años mas,tendre 55. En cuantos años tendre 60?\n"
        msg_dificil ="Un rio se seca durante las temporadas de calor pero se llena en el invierno. En epoca de lluvia se demora 18 dias en llenarse. Cuanto demorara en llenarse la mitad del rio si solo llueve un cuarto de lo que llueve normalmente?\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 38 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 36 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 36 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario
def cuarta_pregunta(nivel, diario):
    valor_respuesta = False
    advertencia = "De hecho, eso no es correcto."
    felicidades = "Debo reconocer que lo haz hecho decentemente hasta aqui."

    while valor_respuesta == False:
        msg_facil = "Tienes tres cajas de frutas. Naranjas, Manzanas y Mezcla. Las tres incorrectamente etiquetadas y solo puedes tomar una fruta de una de las cajas para etiquetarlas correctamente. Que caja escojerias?\n"
        msg_dificil ="\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)
                 
        if respuesta == "salir":
            
            return final,diario

        elif nivel == "1" and respuesta.lower() != "mezcla" and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and respuesta.lower() == "mezcla" and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True
#______________________Aqui vamos con las preguntas_____________________________#  

        elif nivel == "2" and respuesta.lower() == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and respuesta.lower() != 38 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def quinta_pregunta(nivel, diario):
    valor_respuesta = False
    advertencia = "Lamento decirlo, pero estas equivocado."
    felicidades = "Lo haz hecho bien, supongo."

    while valor_respuesta == False:
        msg_facil = "Si tengo 22 años, en 27 años tendre 49. Si pasan 16 años mas,tendre 55. En cuantos años tendre 60?\n"
        msg_dificil ="Cuanto es 10 + 10\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 38 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 38 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def sexta_pregunta(nivel, diario):
    valor_respuesta = False
    advertencia = "Piensalo bien."
    felicidades = "Supongo que no puedo negar que mereces cierto reconocimiento. Felicidades."

    while valor_respuesta == False:
        msg_facil = "Si tengo 22 años, en 27 años tendre 49. Si pasan 16 años mas,tendre 55. En cuantos años tendre 60?\n"
        msg_dificil ="Cuanto es 10 + 10\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 38 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 38 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 38 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def puerta_final(nivel, diario):
    pass

        







def main():




    nombre_juego = "Escape del bosque"
    inicio = "Haz quedado atrapado dentro de una mazmorra, pero no te preocupes, porque hay una manera de salir. Si resuelves todos los acertijos que te realizare y encuentras el patron, entonces podras salir de este lugar.\n" 
   

    final = False
    diario = []
    print(f"Bienvenido a {nombre_juego}\n")
    
    time.sleep(0.5)
    
    jugador = input(f"Cual es tu nombre?\n")
    
    time.sleep(0.5)
    
    print(f"Hola {jugador}")
    

    time.sleep(0.5)
    
    while final == False:
        nivel = input("En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1. Facil\n2. Dificil\n")
        
        time.sleep(1)
        if nivel == "1" or nivel == "2":
            print(inicio)
            final, diario = primera_pregunta(nivel, diario)
            if final == True:
                break
            final, diario = segunda_pregunta(nivel, diario)
            if final == True:
                break
            # final, diario = tercera_pregunta(nivel, diario)
            # if final == True:
            #     break
            # final, diario = cuarta_pregunta(nivel, diario)
            # if final == True:
            #     break
            # final, diario = quinta_pregunta(nivel, diario)
            # if final == True:
            #     break
            # final, diario = sexta_pregunta(nivel, diario)
            # if final == True:
            #     break

            print("Gracias por jugar")

            respuesta = input("Deseas otra partida?(si/no)")
            if respuesta == "no":
                final = True
            else:
                final = False

        else:
            print("valor no valido")    
        
        




       


    

main()