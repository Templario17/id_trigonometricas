#!/usr/bin/env python
#-*- coding: utf-8 -*-

menu = "menu.txt"
banner = "banner.txt"
plantilla_derivada = "formulas/derivadas"
plantilla_cociente = "formulas/iden_cociente"
plantila_pitagorica = "formulas/iden_pitagoricas"
plantilla_reciproca = "formulas/iden_reciprocas"

def leer_derivadas(plantilla_derivada):
    with open (plantilla_derivada, "r") as archivo:
        plantilla_dev = archivo.read()
        return plantilla_dev

def leer_idcociente(plantilla_cociente):
    with open (plantilla_cociente, "r") as archivo:
        plantilla_ic = archivo.read()
        return plantilla_ic

def leer_idpitag(plantila_pitagorica):
    with open (plantila_pitagorica) as archivo:
        plantilla_ip = archivo.read()
        return plantilla_ip
def leer_idrecip(plantilla_reciproca):
    with open(plantilla_reciproca) as archivo:
        archivo.read()

def leer_banner(banner):
    with open(banner, "r") as archivo:
        banner = archivo.read()
        return banner

def leer_menu(menu):
    with open(menu) as archivo:
        plantilla = archivo.read()
        return plantilla

def main():
    print leer_menu(menu)
    opcion = raw_input("ingresa la opcion :")

    if opcion == "1":
        print leer_idcociente(plantilla_cociente)
        print "[*] EXIT..."
    if opcion == "2":
        print leer_idpitag(plantila_pitagorica)
        print "[*]EXIT..."
    elif opcion == "3":
        print leer_idpitag(plantilla_reciproca)
        print "[*] EXIT ..."
    elif opcion == "4":
        print leer_derivadas(plantilla_derivada)
        print "[*] EXIT ..."
    elif opcion == "5":
        print "[*] ha salido correctamente..  bye bye :)!"
        exit()
    else:
        print "elige la opcion correcta 1 al 5  :( !"
    main() # llamada reacursiva


print leer_banner(banner)
main()
