# -*- coding: utf-8 -*-

'''
Created on 06/07/2012

@author: fran
'''
import re


class concepto:
    """
    ~C |{CODIGO\ }|UNIDAD|RESUMEN|{PRECIO\ }|{FECHA\ }|TIPO|CURVA_PRECIO_SIMPLE |CURVA_PRECIO_COMPUESTO |
CODIGO: CODIGO del concepto descrito. Un concepto puede tener varios CODIGOs que actuarán como sinónimos,
este mecanismo permite integrar distintos sistemas de clasificación.
Para distinguir el concepto tipo raíz de un archivo, así como los conceptos tipo capítulo, se ampliará su
CODIGO con los caracteres '##' y '#' respectivamente; quedando dicha notación reflejada obligatoriamante el
el registro tipo ~C ,siendo opcional en los restantes registros del mismo concepto.
Las referencias a un CODIGO con y sin #, se entienden únicas a un mismo concepto.
Unicamente puede haber un concepto raíz en una base de datos u obra, siendo obligatorio que figure.
UNIDAD: Unidad de medida. Existe una relación de unidades de medida recomendadas, elaborada por la
Asociación de Redactores de Bases de Datos de Construcción.
RESUMEN: Resumen del texto descriptivo. Cada soporte indicará el número de caracteres que admite en su campo
resumen.
PRECIO: Precio del concepto. Un concepto puede tener varios precios alternativos que representen distintas
épocas, ámbitos geográficos, etc.
FECHA: Fecha de la última actualización del precio. Cuando haya más de una fecha se asignarán secuencialmente
a cada precio definido, si hay más precios que fechas, los precios sin su correspondiente fecha tomarán la última fecha definida.
Las fechas se definirán en el formato DDMMAA; DD representa el día con dos dígitos, MM el mes y AA el año, si
la fecha tiene menos de 5 dígitos representa mes y año únicamente, si tiene menos de tres, solo el año. Si se identifica la fecha con un número impar de dígitos, se completará con el carácter cero por la izquierda.
TIPO: Tipo de concepto, Inicialmente se reservan los siguientes tipos:
0(Sin clasificar) 1 (Mano de obra), 2 (Maquinaria y medios aux.), 3 (Materiales)
CURVA_PRECIO_SIMPLE: Indicará una curva de variación del precio unitario correspondiente, según propuesta
definida por el Banco de Precios de la Construcción de Aragón (perteneciente a la Diputación General de Aragón).
CURVA_PRECIO_COMPUESTO: incluirá un conjunto de coeficientes de variación de precio en función de la cantidad
utilizada de este precio en la obra. Actualmente utilizados por la base de datos de EDETCO.
    """
    def __init__(self, codigo, unidad, resumen, precio, fecha, tipo, CPS, CPC):
        self.codigo = codigo
        self.unidad = unidad
        self.resumen = resumen
        self.precio = precio
        self.fecha = fecha
        self.tipo = tipo
        self.CPS = CPS
        self.CPC = CPC
    
    def medicion(self):
        print 'Método que calcula medición'

class presupuesto:
    """Es un objeto que representa el presupuesto entero """
    def __init__(self, nombre):
        print 'Creado presupuesto nombrado', nombre

    def leerBC3(self, archivo):
        regs = re.split('~',open(archivo).read())
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

        
        '''
        for concepto in self.conceptos:
            self.dicC.update( {concepto[0]: concepto[1:]})
        '''
        '''
        for n, concepto in enumerate(self.conceptos):
            dicC. {concepto[0]: n}
        '''
    def buscar_concepto(self,codigo):
        for concepto in self.conceptos:
            if concepto[0] == codigo:
                return concepto
            else:
                pass
    def escribir_resumen(self,codigo,resumen):
        print self.buscar_concepto(codigo)
       
    def grabar_BC3(self,archivo):
        f = open(archivgrabarBC3     f.write('~V|SOFT S.A.|FIEBDC-3/2002|Presto 11.02||ANSI|'+'\n')
        f.write(u'~K|\\2\\3\\3\\2\\2\\2\\2\\EUR\\|0|'+'\n')
        for registrosC in [[concepto] + self.conceptos[concepto]  for concepto in self.conceptos]:
            reC = '~C|'
            for tt in registrosC:
                reC = reC + tt +'|'
            #print reC
            f.write(reC+'\n')
        [ f.write(reT) for reT in [ '~T|' + texto +'|' + self.textos[texto] + '|\n' for texto in self.textos]] 
        [ f.write(reD) for reD in [ '~D|' + descomp +'|' + self.descomposiciones[descomp][0] + '|\n' for descomp in self.descomposiciones]] 
        [ f.write(reM) for reM in [ '~M|' + med +'|' + self.mediciones[med][0] + '|\n' for med in self.mediciones]] 

        
        
        '''
        self.conceptos = [[re.split('\|', regC) for regC in re.findall('^C', registro)] for registro in registros]
        '''
'''
pres = presupuesto('pres prueba1')
pres.leerBC3('179-11.bc3')
print pres.conceptos[150]
print len(pres.conceptos)
try:
    print pres.descomposiciones[54]
    print len(pres.descomposiciones)
except IndexError:
    pass
finally:
    pass
print pres.mediciones[54]
print len(pres.mediciones)
print pres.textos[54]
print len(pres.textos)
'''


presBAS = presupuesto('presBAS')
presBAS.leerBC3('179-11.bc3')

#print presBAS.conceptos['18#']
#print presBAS.descomposiciones['18#']
for texto in presBAS.textos:
    print presBAS.textos[texto]
#print presBAS.conceptos['2.7.015']





pres1 = presupuesto('pres1')
pres1.leerBC3('018-12.bc3')


print pres1.textos


for concepto in pres1.conceptos:
    try:
        
        for textoBAS in presBAS.textos:
            if presBAS.textos[textoBAS] == pres1.textos[concepto]:
                print 'Coinciden', textoBAS, 'y', concepto
                print pres1.textos[concepto]
                print presBAS.conceptos[textoBAS][1]
                print pres1.conceptos[concepto]
                pres1.conceptos[concepto][1] = presBAS.conceptos[textoBAS][1]
                print pres1.conceptos[concepto]
    except KeyError:
        pass

pres1.grabar_BC3('018-12_con_resumen.bc3')


print presgrabarBC3siciones
print [ '~D|' + codigo+ '|' + pres1.descomposiciones[codigo][0] + '|' for codigo in pres1.descomposiciones]


# print presBAS.buscar_concepto('T30DA0005')

'''
print len(pres.registros)
print pres.conceptos[:20]
archivo = open('vua1.bc3').read()

registros = re.split('~',archivo)

for registro in registros[:20]:
    if re.search('C|', registro):
        print re.split('\|', registro)[1:-1]
        #c_002 = concepto(re.split('\|', registro)[1:-1])


c_001 = concepto('cod001', 'm3', 'Excavación en zanja', 10.5, '010110', '1', '1', '1')


c_001.medicion()    
print c_001.resumen
'''   