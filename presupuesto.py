# -*- coding: utf-8 -*-

'''
Created on 06/07/2012

@author: fran
'''
import re
from collections import defaultdict

def tree(): return defaultdict(tree)


class presupuesto:
    """
    Es un objeto que representa el presupuesto entero.
    TODO
    Implementar métodos de comprobación de mediciones y presupuesto grabados en cada uno.
    """
    def __init__(self, *archivo):
        try:
            self.leerBC3(archivo)
            print self,'es un presupuesto creado a partir de', archivo[0]
        #except TypeError:
        #    print 'Creado presupuesto sin datos'
        finally:
            pass
        
    def leerBC3(self, archivo):
        """
        Este método lee el archivo BC3 que se el pasa y lo guarda dentro del objeto presupuesto
        Por el momento solo lee los registros tipo C, D, T y M
        TODO
        Incluir los registros V y K.
        Incluir el resto de los registros.
        Decir a que versión puede pertenecer el BC3
        """

        regs = re.split('~',open(archivo[0]).read())
        self.registros = [re.split('\|',reg) for reg in regs]
        
        [regsC, regsD, regsM, regsT] = [{},{},{},{}]
        for reg in self.registros:
            if reg[0] == 'C':
                regsC.update({reg[1]:reg[2:-1]})
            elif reg[0] == 'D':
                try:
                    regsD.update({reg[1]:reg[2:-1]})
                    #regsD.append(reg[1:-1])
                except IndexError:
                    print "No hay descomposiciones"
            elif reg[0] == 'M':
                regsM.update({reg[1]:reg[2:-1]})
                #regsM.append(reg[1:-1])
            elif reg[0] == 'T':
                regsT.update({reg[1]:reg[2:-1][0]})
                #regsT.append(reg[1:-1])
            else:
                pass

        self.conceptos = regsC
        self.descomposiciones = regsD
        self.mediciones = regsM
        self.textos = regsT

        for capitulo in self.descomposiciones:
            if re.search('.*##',capitulo):
                self.importe_tot = float(self.conceptos[capitulo][2])
        
    def grabarBC3(self,archivo):
        """Este método graba los datos del objeto en un archivo BC3
        RESUELTO
        Los carácteres \ hay que ponerlos dobles al grabar y no se graban bien. Esto es importante para
        el formato BC30. Parece que esta resuelto con el prefijo r al string.
        La chapuza para grabar los registro C
        TODO
        La chapuza de los registros V y K.
        """
        f = open(archivo,'w')
        f.write('~V|SOFT S.A.|FIEBDC-3/2002|ARPO-BC3||ANSI|'+'\n')
        f.write(r'~K|\2\3\3\2\2\2\2\EUR\|0|'+'\n')
        
        for concepto in self.conceptos:
            f.write(r'~C|' + concepto + '|' + '|'.join(self.conceptos[concepto]) + '|\n')
        
        for texto in self.textos:
            f.write(r'~T|' + texto + '|' + self.textos[texto] + '|\n')
        
        for descomp in self.descomposiciones:
            f.write(r'~D|' + descomp + '|' + '|'.join(self.descomposiciones[descomp]) + '|\n')
        
        for med in self.mediciones:
            f.write(r'~M|' + med + '|'.join(self.mediciones[med][0]) + '|\n')

    
    def comprobar_importe_total(self):
        for capitulo in self.descomposiciones:
            if re.search('.*##',capitulo):
                self.importe_tot = float(self.conceptos[capitulo][2])



def tree(): return defaultdict(tree)

'''

presBAS = presupuesto('179-11.bc3')


descompRE = re.compile('(.*?)\\\\(.*?)\\\\(.*?)\\\\')
padre = '18#'

arbol ={}

esquema = tree()
esquema = dict()
for padre in presBAS.descomposiciones:
    esquema[padre] = {}
    print "padre",padre
    aa = re.split(descompRE,
               presBAS.descomposiciones[padre][0])[0:-1]
    hijos = [ (a , {}) for a in aa[1::4]]
    esquema[padre].update(hijos)
    #print zip(aa[0::4],aa[1::4],aa[2::4])
    #print aa
    for dd in zip(*[iter(aa)]*4):
        print dd[1:]
print esquema
print "ESQUEMA"


def comp_esq(esquema):
    for cap in esquema.values():
        for clave in cap.keys():
            try:
                cap.update([clave, esquema[clave]])
            except KeyError:
                pass
        comp_esq(cap)
    

esquema2 = comp_esq(esquema)
'''
 
        
    