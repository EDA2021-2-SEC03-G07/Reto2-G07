"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import re
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
import time
default_limit=1000
sys.setrecursionlimit(default_limit*10)
import time
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Mostrar n obras más antiguas de una técnica")
    print("3- Listar cronológicamente las obras según fecha adquisición")
    print("4- Clasificar las obras de un artista por técnica")





#Funciones de inicialización
def loadData(catalog):
    controller.loadData(catalog)

def printreq1(ord_list):
    size_list = lt.size(ord_list)
    print('El número de artistas dentro del rango es:',size_list)
    sub_list = lt.subList(ord_list, 0, lt.size(ord_list))
    print('Los primeros tres artistas son: ')
    for i in range(2,5):
        element = lt.getElement(sub_list,i)
        print(element)
    print('')
    print('Los últimos tres artistas son: ')
    for i in range(0,3):
        element = lt.removeLast(sub_list)
        print(element)

def printreq4(obras_top):
    obras = me.getValue(obras_top)
    sub_list = lt.subList(obras,0,lt.size(obras))
    print('Los primeros 3 buckets son:')
    for i in range(0,3):
        element = lt.getElement(sub_list,i)
        print(element)
    print('')
    print('Los últimos 3 buckets son: ')
    for i in range(0,3):
        element = lt.removeLast(sub_list)
        print(element)
catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        metodo=int(input('Seleccione 1 para Probing y 2 para Chaining:\n'))
        if metodo == 1:
            metodo = 'PROBING'
            factor= 0.7
        if metodo == 2:
            metodo = 'CHAINING'
            factor= 4.0
        print("Cargando información de los archivos ....")
        start_time= time.process_time()
        catalog = controller.initCatalog(metodo,factor)
        controller.loadData(catalog)
        '''print("Estos son los artistas",catalog['Artist_id'])
        print('ESPACIO XD')
        print("Estas son las obras",catalog['Artwork_id'])
        print('ESPACIO XD')
        print("Estas son las obras según las técnicas",catalog["Medium_art"])
        print('ESPACIO XD')
        print("Estas son las obras según la nacionalidad",catalog["Nationalities"])'''
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("Tiempo de carga de datos: ", elapsed_time_mseg, "ms")
        print('El tiempo de ejecución para las nacionalidades es: ')
        print('')
        print('El tiempo de ejecución para los medios es: ')

    
    elif int(inputs[0]) == 2:
        tecnica= input("Ingrese la técnica de interés: ")
        numobras= int(input("Ingrese el número de obras más antiguas que utilizan dicha técnica: "))

        listix= controller.masAntiguas(catalog,numobras,tecnica)
        print(listix)

    elif int(inputs[0]) == 3:
        inicial= input("Ingrese la fecha inicial en formato (AAAA-MM-DD): ")
        final= input("Ingrese la fecha final en formato (AAAA-MM-DD): ")

        info= controller.artworks_in_range(catalog,inicial,final)
        primeros3= info[0]
        ultimos3= info[1]
        size= info[2]
        purchased= info[3]
        
        print("El MoMA adquirió "+ str(size) +" obras entre "+ inicial +" y "+ final +"...")
        print(str(purchased)+" de los cuales fueron comprados.")
        print("Las primeras tres obras en el rango son: ")
        print(primeros3)
        print("Las últimas tres obras en el rango son: ")
        print(ultimos3)

    elif int(inputs[0]) == 4:
        nombre= input("Ingrese el nombre del artista a consultar: ")
        info= controller.artist_techniques(catalog,nombre)
        id= info[0]
        totalobras= info[1]
        totaltecnicas= info[2]
        toptechnique= info[3]
        totaltoptechnique= info[4]
        primeros3= info[5]
        ultimos3= info[6]
        print(nombre+" con ID de MoMA "+ id + " tiene "+ str(totalobras)+" obras con su nombre en el museo...")
        print("Hay "+ str(totaltecnicas) + " técnicas diferentes en sus obras...")
        print("Pero su técnica más utilizada es "+ toptechnique + ", encontrada en "+
                str(totaltoptechnique)+ " de sus obras.")
        print("Las primeras tres obras con esta técnica son:")
        print(primeros3)
        print("Las últimas tres obras con esta técnica son:")
        print(ultimos3)





    elif int(inputs[0]) == 5:
        departamento= input("Ingrese el nombre del departamento a cotizar: ")
        info= controller.transport_artworks(catalog,departamento)
        print("El total de obras para transportar del departamento "+ departamento+" es "+ str(info[0])+"...")
        print("El costo estimado del servicio de transporte sería "+ str(info[1])+ " USD...")
        print("Con un peso estimado total de "+ str(info[2]))
        print("Las cinco obras más antiguas a transportar son...")
        print(info[3])
        print("Las cinco obras más costosas a transportar son...")
        print(info[4])


    elif int(inputs[0]) == 3:
        lowdate = int(input('Ingrese la fecha mínima: \n'))
        highdate = int(input('Ingrese la fecha máxima: \n'))
        req1 = controller.req1(catalog,lowdate,highdate)
        final = printreq1(req1)
        print(final)
    elif int(inputs[0]) == 4:
        req4 = controller.req4(catalog)
        final = printreq4(req4)
    else:
        sys.exit(0)
sys.exit(0)
