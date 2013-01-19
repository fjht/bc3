# -*- coding: utf-8 -*-

'''
Created on 06/07/2012

@author: fran
'''
import re
import nltk
from collections import defaultdict
from nltk.tokenize import PunktWordTokenizer as Tokenizador
from nltk.probability import FreqDist 

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
         

'''
El siguiente código sirve para pasar los textos largo de un presupuesto a otro presupuesto
TODO
Para comprobarlo se iguala simplemente textos largos de un presupuesto y otro.
Esto no funciona especialmente bien puesto que pueden tener la misma información y no el mismo formato.
Habría que implementar un análisis de los textos para así sacar las palabras clave.
'''

presBAS = presupuesto('179-11.bc3')
pres1 = presupuesto('018-12.bc3')
'''

verbose = False
for concepto in pres1.conceptos:
    try:
        for textoBAS in presBAS.textos:
            if presBAS.textos[textoBAS] == pres1.textos[concepto]:
                if verbose:
                    print 'Coinciden', textoBAS, 'y', concepto
                    print pres1.textos[concepto]
                    print presBAS.conceptos[textoBAS][1]
                    print pres1.conceptos[concepto]
                    print pres1.conceptos[concepto]
                pres1.conceptos[concepto][1] = presBAS.conceptos[textoBAS][1]
    except KeyError:
        pass

pres1.grabarBC3('018-12_con_resumen.bc3')
presBAS.grabarBC3('179-11_prueba_exportar.bc03')
'''


todos_textos = ' '.join([pres1.textos[codigo].decode('latin2') for codigo in pres1.textos])
print todos_textos
textos_token = [Tokenizador().tokenize(pres1.textos[codigo].decode('latin2')) 
                for codigo in pres1.textos]
todos_textos_token = Tokenizador().tokenize(todos_textos)


fq1 = FreqDist(textos_token[-6])
fq2 = FreqDist(textos_token[-4])
fqT = FreqDist(todos_textos_token)
distribuciones = {}
for codigo in pres1.textos:
    texto = Tokenizador().tokenize(pres1.textos[codigo].decode('latin2')) 
    fq = FreqDist(texto)
    distribuciones.update({codigo : [fq[token] for token in fqT]})
    #distribuciones.update({codigo : [{token: fq[token]} for token in fqT]})


for distri in distribuciones:
    for dist in [d for d in distribuciones if distribuciones != distri]:
        if (dist != distri and distribuciones[dist] == distribuciones[distri]):
            print dist,'es probable que sea igual a', distri
            print dist, pres1.textos[dist].decode('latin2')
            print distri, pres1.textos[distri].decode('latin2')
