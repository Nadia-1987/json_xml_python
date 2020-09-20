#!/usr/bin/env python
'''
JSON XML [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''
import json
import requests
import xml.etree.ElementTree as ET

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}
    json_data = {
               "nombre": "Nadia",
               "apellido": "Escalzo",
               "dni": 32876689,
               "prendas": [
                        {
                        "prenda": "remeras",
                        "cantidad": 2},
                        {
                        "prenda": "jean",
                        "cantidad": 4                        
                        }
                        ]
                }

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    with open('mi_json_data.json', 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)

    # Observe el archivo y verifique que se almaceno lo deseado
    pass


def ej2():
    # JSON Deserialize
    # Basado en el ejercicio anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en el ej1
    
    with open('mi_json_data.json', 'r') as jsonfile:
        json_data = json.load(jsonfile)

    print('Mostrar el contenido del archivo mi_json_data')
    print(json.dumps(json_data, indent=4))
    
    pass

def ej3():
    # Ejercicio de XML
    # Basado en la estructura de datos del ejercicio 1,
    # crear a mano un archivo ".xml" y generar una estructura
    # lo más parecida al ejercicio 1.
    # El objectivo es que armen un archivo XML al menos
    # una vez para que entiendan como funciona.

    
    

    pass

def ej4():
    # XML Parser
    # Tomar el archivo realizado en el punto anterior
    # e iterar todas las tags del archivo e imprimirlas
    # en pantalla tal como se realizó en el ejemplo de clase.
    # El objectivo es que comprueben que el archivo se realizó
    # correctamente, si la momento de llamar al ElementTree
    # Python lanza algún error, es porque hay problemas en el archivo.
    # Preseten atención al número de fila y al mensaje de error
    # para entender que puede estar mal en el archivo.
    

    tree = ET.parse('mis_datos.xml')
    root = tree.getroot()

    print('Recorrer el archivo XML')
    for child in root:
        print('tag:', child.tag, 'attr:', child.attrib, 'text:', child.text)
        for child2 in child:
            print('tag:', child2.tag, 'attr:', child2.attrib, 'text:', child2.text)

    pass

def ej5():
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url)
    dataset = response.json()

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general.
    # Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".
    # De cada usuario en el total de las 200 entradas contar cuantos títulos
    # completó cada usuario (de los 10 posibles) y armar
    # un gráfico de torta resumiendo la información.

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    usuario_1 = 0
    usuario_2 = 0
    usuario_3 = 0
    usuario_4 = 0
    usuario_5 = 0
    usuario_6 = 0
    usuario_7 = 0
    usuario_8 = 0
    usuario_9 = 0
    usuario_10 = 0

    for user in dataset:
        if user['completed'] == True:
            if user ["userId"] == 1:
                usuario_1 += 1  
            elif user ["userId"] == 2:
                usuario_2 += 1 
            elif user ["userId"] == 3:
                usuario_3 += 1 
            elif user ["userId"] == 4:
                usuario_4 += 1
            elif user ["userId"] == 5:
                usuario_5 += 1 
            elif user ["userId"] == 6:
                usuario_6 += 1    
            elif user ["userId"] == 7:
                usuario_7 += 1
            elif user ["userId"] == 8:
                usuario_8 += 1
            elif user ["userId"] == 9:
                usuario_9 += 1
            elif user ["userId"] == 10:
                usuario_10 += 1
    
    print('la cantidad de titulos del usuario 1 son:', usuario_1)
    print('la cantidad de titulos del usuario 2 son:', usuario_2)
    print('la cantidad de titulos del usuario 3 son:', usuario_3)
    print('la cantidad de titulos del usuario 4 son:', usuario_4)
    print('la cantidad de titulos del usuario 5 son:', usuario_5)
    print('la cantidad de titulos del usuario 6 son:', usuario_6)        
    print('la cantidad de titulos del usuario 7 son:', usuario_7)
    print('la cantidad de titulos del usuario 8 son:', usuario_8)
    print('la cantidad de titulos del usuario 9 son:', usuario_9)
    print('la cantidad de titulos del usuario 10 son:', usuario_10)
        

    # Debe poder graficar dicha información en un gráfico de torta.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    # ej3()
    #ej4()
    ej5()
