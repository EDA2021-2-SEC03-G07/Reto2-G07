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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

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
               'Artwork_id': None}

    catalog['Artist_id'] = mp.newMap(1600, maptype='CHAINING',
                                    loadfactor=4.0)
    catalog['Artwork_id'] = mp.newMap(14000, maptype='CHAINING',
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
    mp.put(catalog['Artwork_id'], artwork['ConstituentID'],artwork)

def addMedium(catalog,artwork):
    #Toca que configures esto para agregar datos
    mp.put(catalog['Medium_art'], artwork['ConstituentID'],artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
