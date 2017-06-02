#!/usr/bin/env python
#-*-* coding: utf-8 -*-
# script que muestra en pantalla las identidades trigonometricas

plantilla_1 = "formulas/iden_cociente"
plantilla_2 = "formulas/iden_pitagoricas"
plantilla_3 = "formulas/iden_reciprocas"

def leer_plantilla_1(plantilla_1):
    with open(plantilla_1, 'r') as archivo:
        archivo = archivo.read()
        return archivo
print leer_plantilla_1(plantilla_1)

def leer_plantilla_2(plantilla_2):
    with open(plantilla_2, 'r') as archivo:
        archivo = archivo.read()
        return archivo
print leer_plantilla_2(plantilla_2)


def leer_plantilla_3(plantilla_3):
    with open(plantilla_3, 'r') as archivo:
        archivo = archivo.read()
        return archivo
print leer_plantilla_3(plantilla_3)
