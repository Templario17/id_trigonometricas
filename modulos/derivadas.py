#!/usr/bin/env python
#-*- coding: utf-8 -*-
# script que muestra plantilla de las derivadas

plantilla = "formulas/derivadas"

#funcion de leer plantilla

def leer_derivadas(plantilla):
    with open(plantilla, 'r') as archivo:
        plantilla = archivo.read()
        return plantilla
        
print leer_derivadas(plantilla)
