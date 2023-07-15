import time
import random

#-------------Patron------------#

def mostrar_patron(patron):
    print("************")
    patron_usuario = "" 
    for numero in patron:
        numero = str(numero)
        print(numero, end=" ")
        patron_usuario = patron_usuario + " " + numero
    return patron_usuario
    print("\n************") 

def definir_patron(nivel, puerta):
    patron = [] 
    
    a = random.randint(1,25)
    b = random.randint(1,25)

    patron = [a, b]

    if nivel == "1":
         for i in range(0,2):
            c = patron[-2] - patron[-1]
            int(c)
            patron.append(c)
    elif nivel == "2":

        for i in range(0,3):
            if patron[-2] % patron[-1] == 0:
                c = patron[-2] + patron[-1]
            else:
                c = patron[-2] - patron[-1]
            int(c)
            patron.append(c)
    
    if puerta == False:
        patron_usuario = mostrar_patron(patron)
        return patron_usuario

    elif puerta == True:
        for i in range(3,0,-1):
            print(patron[0:2])
            advertencia = "Lo siento, no es la respuesta que buscaba"
            ingreso = input("Que numero sigue?\n")
            ingreso = transformar_a_numero(ingreso, advertencia)
            if ingreso == patron[2]:
                print("Felicidades, lograste completar este nivel")
                break
            else:
                print(f"No es la respuesta correcta. Solo te quedan {i-1} intentos.")
        print("Game over, mejor suerte para la proxima.")

#--------------Fin Patron ----------#
#----------Diario-------------#

def agregar_a_diario(patron_usuario, diario):
    terminar = False
    while terminar == False:   
        valor = input(f"Deseas agregar {patron_usuario} a tu diario (si/no)?\n")
        valor = valor.lower()
        if valor == "si":
            diario += [patron_usuario]
            mostrar_diario(diario)
            return diario
        elif valor == "no":
            return diario
    
def mostrar_diario(diario):
    msg_diario = "Deseas revisar tu diario(si/no)?\n"
    terminar = False
    while terminar == False:
        valor = input(msg_diario)
        if valor.lower() == "si":
            print(diario)
            break
        elif valor.lower() == "no":
            break
        else:
            continue

#----------Fin Diario --------------#

#--------------complemento pregunta --------------#

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

#---------Fin complemento pregunta ---------------#

#----------Preguntas-----------------#

def primera_pregunta(nivel, diario, puerta):
    
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
        
         
    patron_usuario = definir_patron(nivel, puerta)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def segunda_pregunta(nivel, diario, puerta):
    valor_respuesta = False
    advertencia = "Vas por mal camino, sigue asi y te quedaras dentro.\n"
    felicidades = "Sigue asi y puede que logres marcharte de este lugar\n"

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
            print("oh no, creo que ingresaste algo mal")

    patron_usuario = definir_patron(nivel, puerta)
    
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def tercera_pregunta(nivel, diario, puerta):
    valor_respuesta = False
    advertencia = "Lamento decirlo, pero estas equivocado."
    felicidades = "Lo haz hecho bien hasta el momento...supongo."

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
        
            
    patron_usuario = definir_patron(nivel, puerta)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def cuarta_pregunta(nivel, diario, puerta):
    valor_respuesta = False
    advertencia = "De hecho, esa no es la respuesta."
    felicidades = "Debo reconocer que lo haz hecho decentemente hasta aqui, aunque el ultimo igual llego a donde estas ahora..."

    while valor_respuesta == False:
        msg_facil = "Tienes tres cajas de frutas. Naranjas, Manzanas y Mezcla. Las tres incorrectamente etiquetadas y solo puedes tomar una fruta de una de las cajas para etiquetarlas correctamente. Que caja escojerias?\n"
        msg_dificil ="Si un par de adultos se come un pollo entero en 10 minutos, cuantas personas harian falta para comer 10 pollos en 20 minutos.\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)
        if respuesta == "salir":
            
            return final,diario

        if isinstance(respuesta, float) == True:
            final = transformar_a_numero(respuesta, advertencia)

        elif nivel == "1" and respuesta.lower() != "mezcla":
            
            print(advertencia)
            
        elif nivel == "1" and respuesta.lower() == "mezcla":
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 20 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 20 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel, puerta)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario
 
def quinta_pregunta(nivel, diario, puerta):
    valor_respuesta = False
    advertencia = "Lamento decirlo, pero tu respuesta es incorrecta..."
    felicidades = "Lo haz hecho bien... supongo."

    while valor_respuesta == False:
        msg_facil = "Un arbol crece de tal manera que dobla su altura todos los años. Cuando alcanza los 100 pies, el arbol tiene 38 años. Que edad tenia el arbol cuando media 50 pies? \n"
        msg_dificil ="En una carrera entre un conejo y un canguro, el conejo le lleva la delantera al canguro por 200 m. Si un salto de canguro equivale a 15 saltos de conejo, y el conejo recorre 12 m por salto, cuantos saltos necesita el canguro para adelantar al conejo(asumiendo que ambos saltan al mismo tiempo)?\n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 37 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 37 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 2 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 2 and isinstance(final, float) == True:
            print(advertencia)
        
            
    patron_usuario = definir_patron(nivel, puerta)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

def sexta_pregunta(nivel, diario, puerta):
    valor_respuesta = False
    advertencia = "yo que tu lo pienso mejor, si realmente quieres salir de este lugar..."
    felicidades = "no puedo evitar felicitarte, superaste al jugador que más pudo avanzar.. Felicidades."

    while valor_respuesta == False:
        msg_facil = "Seis maquinas pueden hacer 6 ruedas en seis minutos. Cuanto minutos les tomara a 30 maquinas hacer 30 ruedas?\n"
        msg_dificil ="Dos trenes van por la misma via pero en direcciones opuestas. Si uno de los trenes va a 120 km y el otro a 180 km/h. Si estan a 60 km el uno del otro, a cuantos kilometros de distancia estaran un minuto antes de chocar \n"
        
        if nivel == "1":
            respuesta = input(msg_facil)
        elif nivel == "2":    
            respuesta = input(msg_dificil)

        
        final = transformar_a_numero(respuesta, advertencia)
        
        if final == True:
            
            return final,diario

        elif nivel == "1" and final != 6 and isinstance(final, float) == True:
            
            print(advertencia)
            
        elif nivel == "1" and final == 6 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final == 5 and isinstance(final, float) == True:
            print(felicidades)
            valor_respuesta = True

        elif nivel == "2" and final != 5 and isinstance(final, float) == True:
            print(advertencia)
              
    patron_usuario = definir_patron(nivel,puerta)
   
    diario = agregar_a_diario(patron_usuario, diario)
    
    final = False

    return final, diario

#----------------------------fin preguntas----------------------
#----------------------------desafio final--------------------

def puerta_final(nivel, diario, puerta):

    print("Lo haz hecho bien, tanto asi que finalmente haz llegado al desafio final. ahora para salir debes encontrar el patron en los numeros dados. Te dare dos numeros, y tendras que este en la siguiente pregunta de acuerdo al patron.")
    mostrar_diario(diario)
    definir_patron(nivel, puerta)
#-------------------------fin desafio final--------------------
#------------------------fin funciones juego-----------------

    #---------------Funcion main----------------
def main():
    nombre_juego = "Escape de la mazmorra"
    inicio = "Haz quedado atrapado dentro de una mazmorra, pero no te preocupes, porque hay una manera de salir. Si resuelves todos los acertijos que te realizare y encuentras el patron, entonces podras salir de este lugar.\n" 
    

    final = False
    diario = []
    print(f"Bienvenido a {nombre_juego}\n")
        
    time.sleep(0.5)
        
    jugador = input(f"Cual seria tu nombre jugador n*300?\n")
        
    time.sleep(0.5)
        
    print(f"Hola {jugador}")
        
    time.sleep(0.5)
        
    while final == False:
            puerta = False
            nivel = input("En que nivel deseas jugar(Ingresa el numero con tu alternativa.)\n1. Facil\n2. Dificil\n")
            
            time.sleep(1)
            if nivel == "1" or nivel == "2":
                print(inicio)
                final, diario = primera_pregunta(nivel, diario, puerta)
                if final == True:
                    break
                final, diario = segunda_pregunta(nivel, diario, puerta)
                if final == True:
                    break
                final, diario = tercera_pregunta(nivel, diario, puerta)
                if final == True:
                    break
                final, diario = cuarta_pregunta(nivel, diario, puerta)
                if final == True:
                    break
                final, diario = quinta_pregunta(nivel, diario, puerta)
                if final == True:
                    break
                final, diario = sexta_pregunta(nivel, diario,  puerta)
                if final == True:
                    break
                puerta = True
                puerta_final(nivel, diario, puerta)
                print("Gracias por jugar con nosotros")

                respuesta = input("Deseas otra partida?(si/no)")
                if respuesta == "no":
                    final = True
                else:
                    final = False

            else:
                print("valor no valido")    
            
        #---------------------Fin funcion main----------------
main()