"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
import re
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    #Son más de 90000 ARTISTAS para el large
    #Son más de 200000 OBRAS para el large
    catalog = {'Artist_id': None,
               'Medium_art':None,
               'Nationality': None,
               'Artwork_id': None}

    catalog['Artist_id'] = mp.newMap(1600, maptype='CHAINING',
                                    loadfactor=4.0)
    catalog['Artwork_id'] = mp.newMap(14000, maptype='CHAINING',
                                    loadfactor=4.0 )
    catalog['Nationality'] = mp.newMap(1, maptype='CHAINING',
                                    loadfactor=4.0 )
    catalog['Medium_art'] = mp.newMap(800, maptype='CHAINING',
                                    loadfactor=4.0 )
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    if artist["Nationality"] == "":
        artist["Nationality"]= "Unknown"
    mp.put(catalog['Artist_id'], artist['ConstituentID'],artist)

def addArtwork(catalog,artwork):
    if artwork["DateAcquired"] == "":
        artwork["DateAcquired"] = "1800-01-01"
    new_Id = artwork['ConstituentID']
    new_Id = re.sub("\[|\]", "", new_Id)
    mp.put(catalog['Artwork_id'], new_Id,artwork)

def addMedium(catalog,artwork):
    if artwork["Medium"] == "":
        artwork["Medium"]= "Unknown"
    if mp.contains(catalog["Medium_art"], artwork["Medium"]) == False:
        listix= lt.newList("ARRAY_LIST")
        lt.addLast(listix, artwork)
        mp.put(catalog['Medium_art'], artwork["Medium"], listix)
    else:
        llave= artwork["Medium"]
        pareja= mp.get(catalog["Medium_art"],llave)
        lt.addLast(me.getValue(pareja),artwork)

def addNationality(catalog, artist):
    """a = '[1921],[703]'
    b = 1921
    '['+b+']' = [1921]
    for i in a.split(','):    YA TENGO TODOO PARA REALIZAR LA ADICIÓN DE DATOS
        print(i)
        if '[1921]' == i:
            print('YES')
            """
    artworks = catalog['Artwork_id']
    nationality = catalog['Nationality']
    if artist['Nationality'] == '':
        artist['Nationality'] = 'Unknown'
    #YA TENGO LA COMPARACION DE LOS CONSTITUENT_ID
    #LO QUE FALTA POR HACER ES QUE SE AGREGUEN CORRECTAMENTE CADA OBRA SEGÚN SU NACIONALIDAD
    if mp.contains(catalog['Nationality'],artist['Nationality']) == False:
        entry = mp.get(artworks,artist['ConstituentID'])
        if entry != None:
            lista_map = lt.newList('ARRAY_LIST')
            añadir = me.getValue(entry)
            lt.addLast(lista_map, añadir)   
            mp.put(catalog['Nationality'], artist['Nationality'], lista_map)
# Funciones para creacion de datos





# Funciones de comparación

def cmpArtworkByDate(artwork1, artwork2):
    date1 = artwork1["Date"]
    date2 = artwork2["Date"]
    return date1 < date2

# Funciones de consulta

def masAntiguas(catalog,numobras, tecnica):
    pareja= mp.get(catalog["Medium_art"],tecnica)
    copia_catalogo= me.getValue(pareja).copy()
    ordered_list= merge.sort(copia_catalogo, cmpArtworkByDate)

    lista_final= lt.newList('ARRAY_LIST')
    i= 1
    while i <= numobras:
        x = lt.getElement(ordered_list,i)
        lt.addLast(lista_final, x)
        i+= 1

    return lista_final


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
