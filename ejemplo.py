#Aquí importo librerías
#Las librerías son conjuntos de funciones ya hechas, INVESTIGAR
import os
import sys

#Comentario una línea

'''
Comentario multilínea, todo este párrafo es comentario.

def: Voy a declarar una función, a continuación tiene que venir su nombre
def getNombre():
             
'''
def getNombre():

    nombre = ''
    print ("Escríbeme tu nombre:", end="")
    #TODO: Captar la entrada por teclado para recibir el nombre del usuario
    nombre = input() # Guardo lo que me ha entrado por teclado en la variable
    #TODO 2: Probar que el usuario ha puesto su nombre
    if(not nombre): #Todo lo que no esté vacío o sea 0, es verdadero
        #TODO 3: Decirle al usuario que no ha puesto su nombre
        return
    print(f'Hola {nombre}.')

    return nombre

#               argumentos de la función
def getApellido(nombre = ''):
    apellido = ''
    print('Dime tu apellido: ')
    apellido = input()
    print(f'Hola tu nombre y tu apellidos son {nombre} {apellido}')

def getEdad():
    edad = ''
    print('Tu edad es: ')
    edad = input()
    print(f'Tu edad es: ')


# En cualquier lenguaje de programación, el punto de entrada al programa, Aquí empezamos la ejecución!
def main():
    # llama a getNombre, lo que te devuelva, lo guardas en mi variable nombreMain
                nombreMain = getNombre()
    getApellido(nombreMain)

# Boilerplate de Python, TODO:investigar
if __name__ == '__main__':
    main()

'''
PARA EJECUTAR:
    Moverme al directorio donde está el script:
    cd /opt/lampp/htdocs/misPaginas/PaginasdePruebaCSS_2/Phyton
    python3 ejemplo.py
'''
