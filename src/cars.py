#-*- coding: utf-8 -*-

from collections import namedtuple
import csv
from datetime import datetime

from matplotlib import pyplot as plt
from parsers import *


Cars = namedtuple("Cars","datetime,make,model,year,engine,mileage,price,fuel_type,new")


#Entrega 1


def leer_csv(fichero):
    car=[]
    with open(fichero,encoding="utf-8") as f:
        lector=csv.reader(f,delimiter=";")
        next(lector)
        for e in lector:
            date=datetime.strptime(e[0],"%m/%d/%Y").date()
            make=e[1]
            model=e[2]
            year=int(e[3])
            engine=float(e[4])
            mileage=float(e[5])
            price=float(e[6])
            fuel_type=e[7]
            new=parsebool(e[8])
            tupla=Cars(date,make,model,year,engine,mileage,price,fuel_type,new)
            car.append(tupla)
    return car



#Entrega 2


#----- BLOQUE 1 ---------------------------------------------------------------------------


def filtrar_marca_modelo(fichero, marca):
    conj=set()
    for x in fichero:
        if x.make == marca:
            tupla=(x.model)
            conj.add(tupla)
    return (marca,conj)


def calcular_media_precio_marca(fichero,marca):
    lista=[]
    for x in fichero:
        if x.make == marca:
            tupla=(x.price)
            lista.append(tupla)
    media = len(lista)*1000/2
    return media

#----- BLOQUE 2 ---------------------------------------------------------------------------

"Funcion auxiliar"

def filtro_año_kilom(fichero,año):
    lista=[]
    for x in fichero:
        if año == x.year:
            tupla=(x.year, x.mileage)
            lista.append(tupla)
    return lista

def maximo_kilom_por_año(fichero,año=None):
    if año != None:
        fichero=filtro_año_kilom(fichero,año)
        lista=[x for x in fichero]
        maximo=max(lista)
    return maximo


def n_precio_fuel(fichero, fuel, n):
    lista=[]
    for x in fichero:
        if fuel==x.fuel_type:
            tupla=(x.price*1000)
            lista.append(tupla)
    return sorted(lista, reverse=True)[:n]

def dicc_marca_nuevo(fichero, año, nuevo):
    
    dicc=dict()
    for x in fichero:
        if año == x.year and x.new == nuevo:
            if x.make in dicc:
                dicc[x.make].append(x.new)
          
            else:
                dicc[x.make]=[x.new]

    
    for k,v in dicc.items():
       dicc[k] = len(v)
    return dicc


#----- BLOQUE 3 ---------------------------------------------------------------------------


def contar_km_segun_fuel_por_año(fichero,año):
    dicc={}
    for x in fichero:
        if año == x.year:        
            if x.fuel_type in dicc: 
                dicc[x.fuel_type]+=[x.mileage]
            else:
                dicc[x.fuel_type]=[x.mileage]

    for k,v in dicc.items():
        dicc[k]= sum(v)    
    return dicc

def max_km_fuel_año(fichero,año):
    dicc=contar_km_segun_fuel_por_año(fichero,año)
    claves=dicc.values()
    maximo=max(claves)
    minimo=min(claves)
    return maximo,minimo
#F.Aux

def precio_año(fichero):
    dicc={}
    for x in fichero:
        c=x.year
        if c in dicc:
            dicc[c] +=[x.price]
        else:
            dicc[c] = [x.price]
    for k,v in dicc.items():
        dicc[k]= sum(v)  
    return sorted(dicc.items(),key=lambda x:x[0],reverse=True)
def dicc_porcentaje_km_por_año(fichero,año):
    total=dict(precio_año(fichero))
    dicc={}
    for x in fichero:
        c = x.make
        if año in total:
            if c in dicc:
                dicc[c] += x.price
            else:
                dicc[c] = x.price
    for key in dicc:
        dicc[key] = dicc[key]*100 / total[año]
    return dicc

def dicc_top_n_coches_por_motor(fichero, n=3):
    c = sorted({x.engine for x in fichero})
    dicc = {clave : 0 for clave in c}
    for k in dicc:
        dicc[k] = sorted([(x.make) for x in fichero if x.engine == k])[:n]
    return dicc


#----- BLOQUE 4 ---------------------------------------------------------------------------
def filtrar_año_precio(fichero, año):
    conj=set()
    for x in fichero:
        if x.year == año:
            tupla=(año,x.price)
            conj.add(tupla)
    return (conj)
def grafica(fichero,año):
    lista_año = filtrar_año_precio(fichero,año)
    lista_precio = filtrar_año_precio(fichero,año)
    lista_año, lista_precio = zip(*filtrar_año_precio(fichero,año))
    print(lista_año)
    print(lista_precio)
    plt.plot(lista_año,lista_precio)

    return plt.show()

















