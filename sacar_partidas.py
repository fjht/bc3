# -*- coding: utf-8 -*-

'''
Created on 26/12/2012

@author: fran

Este programa es para sacar todas las partidas de los bc3 de un presupuesto.
Calcula el peso de la partida en el total del presupuesto.



'''
import re
from presupuesto import presupuesto

presBAS = presupuesto('bc3s/24649_2258.bc3')

descomps = presBAS.descomposiciones
print "Descomposiciones", descomps

arbol = {}

while len(descomps) >= 1:
    nodo = descomps.keys()[0]
    print nodo, [cod[0] for cod in re.findall(r'(.*?)\\(.*?)\\(.*?)\\',descomps[nodo][0])]
    
    descomps.pop(nodo)

arbol = {"raiz": {
                  'C01': {
                          'C01.01':{},
                          'C01.02':{}
                          },
                  'C02': {
                          'C02.01':{},
                          'C02.02':{},
                          'C02.03':{}
                          }
                  }
         }

print arbol.keys()

'''
for concepto in presBAS.conceptos:
    if re.search('.*##',concepto):
        print "Total presupuesto", presBAS.conceptos[concepto]
    elif re.search('.*#', concepto):
        print "Capítulo", presBAS.conceptos[concepto]


for capitulo in presBAS.descomposiciones:
    if re.search('.*##',capitulo):
        print "Total presupuesto", re.split(r'((.*?)\\){3}',presBAS.descomposiciones[capitulo][0])
        print presBAS.descomposiciones[capitulo][0]

print "comienzo"
print
print
for capitulo in presBAS.descomposiciones:
    if re.search('.*##',capitulo):
        print "Total presupuesto", re.split(r'((.*?)\\){3}',presBAS.descomposiciones[capitulo][0])
        print presBAS.descomposiciones[capitulo][0]
    elif re.search('.*#', capitulo):
        partidas = [ re.findall(r"(.*?)\\",partida[0]) for partida in 
                    re.findall(r"(((.*?)\\){3})",presBAS.descomposiciones[capitulo][0])]
        print "Capítulo", capitulo, presBAS.conceptos[capitulo]
        importe = 0.
        for partida in partidas:
            print partida[0], presBAS.conceptos[partida[0]], partida[2], "*", presBAS.conceptos[partida[0]][2], "=",
            imp = float(partida[2]) * float(presBAS.conceptos[partida[0]][2])
            print imp, imp / presBAS.importe_tot
            importe = importe + imp
        print "Importe capítulo", importe
        print presBAS.descomposiciones[capitulo][0]

print "importe total", presBAS.importe_tot

arbol = {}
descomposiciones = []
for nodo in presBAS.descomposiciones:
    descomposicion = re.findall(r'(.*?)\\(.*?)\\(.*?)\\',presBAS.descomposiciones[nodo][0])
    descomposiciones = descomposiciones + [ [nodo, descomposicion]]
    if re.match('.*##',nodo):
        raiz = {nodo: descomposicion}
    elif re.match('.*#',nodo):
        capitulos = {nodo: descomposicion}    
print descomposiciones
print "Capítulos"
print capitulos


for concepto in presBAS.conceptos:
    for descomposicion in descomposiciones:
        print descomposicion


def prueba(descomp):
    for cap in descomp.keys():
        print cap 
        for scap in raiz[cap]:
            prueba(scap)
            print scap



for capitulo in [cap for cap in descomposiciones if re.search('.*#', cap[0])]:
    print capitulo
'''

