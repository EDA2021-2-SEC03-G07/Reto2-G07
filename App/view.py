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
default_limit=1000
sys.setrecursionlimit(default_limit*10)

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

#Funciones de inicialización
def loadData(catlog):
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        metodo=int(input('Seleccione 1 para Probing y 2 para Chaining:\n'))
        if metodo == 1:
            metodo = 'PROBING'
            factor= 0.5
        if metodo == 2:
            metodo = 'CHAINING'
            factor= 4.0
        catalog = controller.initCatalog(metodo,factor)
        controller.loadData(catalog)
        '''print("Estos son los artistas",catalog['Artist_id'])
        print('ESPACIO XD')
        print("Estas son las obras",catalog['Artwork_id'])
        print('ESPACIO XD')
        print("Estas son las obras según las técnicas",catalog["Medium_art"])
        print('ESPACIO XD')'''
        print("Estas son las obras según la nacionalidad",catalog["Nationalities"])
        a = mp.keySet(catalog["Nationalities"])
        print(a)
    
    elif int(inputs[0]) == 2:
        tecnica= input("Ingrese la técnica de interés: ")
        numobras= int(input("Ingrese el número de obras más antiguas que utilizan dicha técnica: "))

        listix= controller.masAntiguas(catalog,numobras,tecnica)
        print(listix)

    else:
        sys.exit(0)
sys.exit(0)
