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


from DISClib.DataStructures.chaininghashtable import put
#from typing import final
from DISClib.DataStructures.arraylist import size, subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
import re
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(metodo,factor):
    #Son más de 90000 ARTISTAS para el large
    #Son más de 200000 OBRAS para el large
    catalog = {'Artist': None,
               'Artwork': None,
               'Artist_id': None,
               'Artwork_id': None,
               'Medium_art':None,
               'Nationalities': None}

    catalog['Artist'] = lt.newList('ARRAY_LIST')
    catalog['Artwork'] = lt.newList()

    artwork_size = lt.size(catalog['Artwork'])
    artist_size = lt.size(catalog['Artist'])

    catalog['Artist_id'] = mp.newMap(artist_size, maptype=metodo,
                                    loadfactor=factor)
    catalog['Artwork_id'] = mp.newMap(artwork_size, maptype=metodo,
                                    loadfactor=factor)
    catalog["Departments"] = mp.newMap(12, maptype=metodo,
                                    loadfactor=factor)
    catalog['Medium_art'] = mp.newMap(artwork_size, maptype= metodo,
                                    loadfactor=factor)
    catalog['Nationalities'] = mp.newMap(artist_size, maptype= metodo,
                                    loadfactor=factor)
    catalog['Birthday_artist'] = mp.newMap(artist_size, maptype=metodo,
                                    loadfactor= factor)
    catalog['Artist_name'] = mp.newMap(artist_size, maptype=metodo,
                                    loadfactor= factor )
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):
    if artist["Nationality"] == "":
        artist["Nationality"]= "Unknown"
    lt.addLast(catalog['Artist'], artist)
    mp.put(catalog['Artist_id'], artist['ConstituentID'],artist)
    mp.put(catalog["Artist_name"],artist["DisplayName"],artist["ConstituentID"])

    mp.put(catalog["Artist_name"],artist["DisplayName"],artist["ConstituentID"])

def addArtwork(catalog,artwork):
    lt.addLast(catalog['Artwork'], artwork)
    if artwork["DateAcquired"] == "":
        artwork["DateAcquired"] = "1800-01-01"
    new_Id = artwork['ConstituentID']   
    new_Id = re.sub("\[|\]", "", new_Id)
    #mp.put(catalog['Artwork_id'], new_Id,artwork)
    if mp.contains(catalog["Artwork_id"],new_Id) == False:
        obras_id= lt.newList("ARRAY_LIST")
        lt.addLast(obras_id,artwork)
        mp.put(catalog['Artwork_id'],new_Id,obras_id)
    else:
        entry= mp.get(catalog["Artwork_id"],new_Id)
        if entry != None:
            lista= me.getValue(entry)
            lt.addLast(lista,artwork)

    if mp.contains(catalog["Departments"],artwork["Department"]) == False:
        obras_dep= lt.newList("ARRAY_LIST")
        lt.addLast(obras_dep,artwork)
        mp.put(catalog["Departments"],artwork["Department"],obras_dep)
    else:
        entry= mp.get(catalog["Departments"],artwork["Department"])
        if entry != None:
            lista= me.getValue(entry)
            lt.addLast(lista,artwork)

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
    artworks = catalog['Artwork_id']
    nationality = catalog['Nationalities']
    if artist['Nationality'] == '':
        artist['Nationality'] = 'Unknown'
    #YA TENGO LA COMPARACION DE LOS CONSTITUENT_ID
    #LO QUE FALTA POR HACER ES QUE SE AGREGUEN CORRECTAMENTE CADA OBRA SEGÚN SU NACIONALIDAD
    if mp.contains(catalog['Nationalities'],artist['Nationality']) == False:
        entry = mp.get(artworks,artist['ConstituentID'])
        if entry != None:
            lista_map = lt.newList('ARRAY_LIST')
            añadir = me.getValue(entry)
            lt.addLast(lista_map, añadir)   
            mp.put(catalog['Nationalities'], artist['Nationality'], lista_map)
    else:
        entry = mp.get(artworks,artist['ConstituentID'])
        if entry != None:
            añadir = me.getValue(entry)
            entry2= mp.get(nationality,artist['Nationality'])
            añadir_lista = me.getValue(entry2)
            lt.addLast(añadir_lista, añadir)

# Funciones de comparación

def cmpArtworkByDate(artwork1, artwork2):
    date1 = artwork1["Date"]
    if date1 == "":
        date1= "3000"
    date2 = artwork2["Date"]
    if date1 == "":
        date1= "3000"
    return date1 < date2

def cmpArtworkByDateAcquired(artwork1, artwork2):
    date1 = time.strptime(artwork1['DateAcquired'], "%Y-%m-%d")
    date2 = time.strptime(artwork2['DateAcquired'], "%Y-%m-%d")
    return date1 < date2

def cmpArtworkByCost(artwork1, artwork2):
    cost1= artwork1["Cost"]
    cost2= artwork2["Cost"]
    return cost1 > cost2
def cmpbirthday(artist1, artist2):
    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

def cmptop(top1, top2):
    return int(top1['#Obras']) > int(top2['#Obras'])

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

def req1(catalog, lowdate, highdate):
    lt_artist = catalog['Artist']
    sorted_artist = lt.newList()
    final_list = lt.newList()
    for date in lt.iterator(lt_artist):
        if int(date['BeginDate']) >= lowdate and int(date['BeginDate']) <= highdate:
            lt.addLast(sorted_artist,date)
    sorted_artist = merge.sort(sorted_artist,cmpbirthday)
    for element in lt.iterator(sorted_artist):
        if element['EndDate'] == '0':
            element['EndDate'] = 'Unknown'
        dict_print = {}
        dict_print['Nombre'] = element['DisplayName']
        dict_print['Nacimiento'] = element['BeginDate']
        dict_print['Fallecimiento'] = element['EndDate']
        dict_print['Nacionalidad'] = element['Nationality']
        dict_print['Género'] = element['Gender']
        lt.addLast(final_list,dict_print)
    return final_list

#Requerimiento 4 por Jesed
def req4(catalog):
    #No sé que hacer con el artworks xd
    countrys = catalog['Nationalities']
    #top_list = mp.newMap(mp.size(countrys),maptype='CHAINING',loadfactor=4.0)
    top_list = lt.newList()
    lista_countrys = mp.keySet(countrys)
    for actual_c in lt.iterator(lista_countrys):
        llave_valor = mp.get(countrys,actual_c)['value']
        size_country = 0
        for index in lt.iterator(llave_valor):
            size = lt.size(index)
            size_country += size
        agregar = {'Nacionalidad':actual_c,
                    '#Obras': size_country}
        #mp.put(top_list,actual_c,size_country)
        lt.addLast(top_list, agregar)
    top_ord = top_list
    top_ord = merge.sort(top_ord,cmptop)
    final_lt = lt.newList()
    i = 0
    for top in lt.iterator(top_ord):
        while i < 10:
            lt.addLast(final_lt, top)
            i += 1
    for top1 in range(0,1):
        top1 = lt.getElement(final_lt,top1)
        top1 = mp.get(countrys, top1['Nacionalidad'])
    return top1

def req6(Número_Artist, lowdate, highdate):
 pass
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento


# Funcion req2
def artworks_in_range(catalog,inicial,final):
    lista_obras= mp.valueSet(catalog["Artwork_id"])
    lista_final_obras= lt.newList("ARRAY_LIST")
    for lista in lt.iterator(lista_obras):
        for obra in lt.iterator(lista):
            lt.addLast(lista_final_obras,obra)

    ordered= merge.sort(lista_final_obras,cmpArtworkByDateAcquired)

    fechainicial= time.strptime(inicial,"%Y-%m-%d")
    fechafinal= time.strptime(final,"%Y-%m-%d")
    listix= lt.newList("ARRAY_LIST")
    for artwork in lt.iterator(ordered):
        if time.strptime(artwork["DateAcquired"],"%Y-%m-%d") >= fechainicial and time.strptime(artwork["DateAcquired"],"%Y-%m-%d") <= fechafinal:
            lt.addLast(listix,artwork)
    
    cont= 0
    for artwork in lt.iterator(listix):
        if artwork["CreditLine"].lower().find("purchase") >= 0:
            cont+= 1

    primeros3= lt.subList(listix,1,3)
    ultimos3= lt.subList(listix,-2,3)

    return primeros3, ultimos3, lt.size(listix), cont



# Funcion req3
def artist_techniques(catalog,nombre):
    id= mp.get(catalog["Artist_name"],nombre)
    constituent= id["value"]
    obras= mp.get(catalog["Artwork_id"],constituent)
    totalobras= lt.size(obras["value"])

    mapa_obras_tecnicas= mp.newMap(500, maptype="CHAINING", loadfactor=1.0)
    dict_contador_tecnicas= {}
    for obra in lt.iterator(obras["value"]):
        if obra["Medium"] not in dict_contador_tecnicas.keys():
            dict_contador_tecnicas[obra["Medium"]]= 1
        else:
            dict_contador_tecnicas[obra["Medium"]]+= 1

        if mp.contains(mapa_obras_tecnicas,obra["Medium"]) == False:
            lista_tecnica= lt.newList("ARRAY_LIST")
            lt.addLast(lista_tecnica,obra)
            mp.put(mapa_obras_tecnicas,obra["Medium"],lista_tecnica)
        else:
            entry= mp.get(mapa_obras_tecnicas,obra["Medium"])
            if entry != None:
                lista= me.getValue(entry)
                lt.addLast(lista,obra)

    totaltecnicas= mp.size(mapa_obras_tecnicas)
    toptechnique= max(dict_contador_tecnicas,key=dict_contador_tecnicas.get)

    entry= mp.get(mapa_obras_tecnicas,toptechnique)
    obras_toptechnique= me.getValue(entry)
    totaltoptechnique= lt.size(obras_toptechnique)

    primeros3= lt.subList(obras_toptechnique,1,3)
    ultimos3= lt.subList(obras_toptechnique,-2,3)

    return constituent, totalobras, totaltecnicas, toptechnique, totaltoptechnique, primeros3, ultimos3


# Funcion req5
def transport_artworks(catalog,departamento):
    lista_departamentos= mp.keySet(catalog["Departments"])
    for department in lt.iterator(lista_departamentos):
        if department == departamento:
            entry= mp.get(catalog["Departments"],department)        
            obras_departamento= entry["value"]

    totaldepartamento= lt.size(obras_departamento)
    sorted= merge.sort(obras_departamento,cmpArtworkByDate)


    tarifa= 72.00
    costo_total= 0
    peso_total= 0
    for obra in lt.iterator(sorted):
        weight= obra["Weight (kg)"]
        width= obra["Width (cm)"]
        length= obra["Length (cm)"]
        height= obra["Height (cm)"]
        diameter = obra["Diameter (cm)"]
        circumference = obra["Circumference (cm)"]
        depth = obra["Depth (cm)"]

        if weight != "":
            kg= float(weight)*tarifa
            peso_total+= float(weight)
        else:
            kg= 0

        if height != "" and width != "":
            m2= (float(height)/100)*(float(width)/100)*tarifa
        elif height != "" and length != "":
            m2= (float(height)/100)*(float(length)/100)*tarifa
        elif height != "" and depth != "":
            m2= (float(height)/100)*(float(depth)/100)*tarifa
        elif length != "" and width != "":
            m2= (float(length)/100)*(float(width)/100)*tarifa
        elif length != "" and depth != "":
            m2= (float(length)/100)*(float(depth)/100)*tarifa
        elif height != "" and depth != "":
            m2= (float(height)/100)*(float(depth)/100)*tarifa
        elif width != "" and depth != "":
            m2= (float(width)/100)*(float(depth)/100)*tarifa
        elif circumference != "":
            m2= (((float(circumference)/100)/(2*3.14))**2)*3.14*tarifa
        elif diameter != "":
            m2= (((float(diameter)/100)/2)**2)*3.14*tarifa
        else:
            m2= 0
        
        if height != "" and width != "" and length != "":
            m3= (float(height)/100)*(float(width)/100)*(float(length)/100)*tarifa
        elif height != "" and width != "" and depth != "":
            m3= (float(height)/100)*(float(width)/100)*(float(depth)/100)*tarifa
        elif height != "" and length != "" and depth != "":
            m3= (float(height)/100)*(float(length)/100)*(float(depth)/100)*tarifa
        elif width != "" and length != "" and depth != "":
            m3= (float(width)/100)*(float(length)/100)*(float(depth)/100)*tarifa
        elif diameter != "" and depth != "":
            m3= (((float(diameter)/100)/2)**2)*3.14*(float(depth)/100)*tarifa
        elif diameter != "" and height != "":
            m3= (((float(diameter)/100)/2)**2)*3.14*(float(height)/100)*tarifa
        elif diameter != "" and width != "":
            m3= (((float(diameter)/100)/2)**2)*3.14*(float(width)/100)*tarifa
        elif diameter != "" and length != "":
            m3= (((float(diameter)/100)/2)**2)*3.14*(float(length)/100)*tarifa
        else:
            m3= 0

        costo_maximo= max(kg,m2,m3)
        if costo_maximo == 0.0:
            costo_maximo= 48.00
        
        costo_total+= costo_maximo
        obra["Cost"]= round(costo_maximo,2)

    lista_antiguos= lt.subList(sorted,1,5)
    lista_costosos= merge.sort(sorted.copy(),cmpArtworkByCost)
    lista_costosos5= lt.subList(lista_costosos,1,5)


    return totaldepartamento, round(costo_total,2), peso_total, lista_antiguos, lista_costosos5


