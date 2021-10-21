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
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import re
import time
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(metodo,factor):

    catalog = model.newCatalog(metodo,factor)
    return catalog

# Funciones para agregar informacion al catalogo
def loadData(catalog):

    loadArtist(catalog)
    loadArtwork(catalog)
    loadNationality(catalog)
    loadMediums(catalog)


# Funciones para creacion de datos
def loadArtist(catalog):
    artistfile = cf.data_dir + 'MoMa/Artists-utf8-10pct.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    
def loadArtwork(catalog):
    artworkfile = cf.data_dir + 'MoMa/Artworks-utf8-10pct.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def loadMediums(catalog):
    artworkfile = cf.data_dir + 'MoMa/Artworks-utf8-10pct.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
       model.addMedium(catalog, artwork)
def loadNationality(catalog):
    artistfile = cf.data_dir + 'MoMa/Artists-utf8-10pct.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addNationality(catalog, artist)


# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def masAntiguas(catalog,numobras,tecnica):
    info= model.masAntiguas(catalog,numobras,tecnica)
    return info

def req1(catalog, lowdate,highdate):
    start_time = time.process_time()
    resultado = model.req1(catalog,lowdate,highdate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print('El tiempo fue que tardó: ', elapsed_time_mseg, 'ms')
    return resultado

def req4(catalog):
    start_time = time.process_time()
    resultado = model.req4(catalog)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    print('El tiempo fue que tardó: ', elapsed_time_mseg, 'ms')
    return resultado

#Funciones de comparación
