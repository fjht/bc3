# -*- coding: utf-8 -*-

'''
Created on 02/11/2012

@author: fran
'''


import re
from types import NoneType

texto = open('04 Presupuesto y mediciones.txt').read().decode('iso-8859-1').encode('utf8')
#print texto[:100000]
'''
for pag in re.split('CÓDIGO  DESCRIPCIÓN  UDS  LONGITUD ANCHURA ALTURA  PARCIALES  CANTIDAD  PRECIO  IMPORTE',
              texto):
    print pag
'''
'''
for cod_dec in [ re.sub("PRESUPUESTO Y MEDICIONES[\w\W]*IMPORTE", '', trozo) for trozo in 
                re.split('([0-9]{2}\.+[0-9]{2})', texto)]:
    print cod_dec
    #print re.search('^PRESUPUESTO Y MEDICIONES[\w\W]*IMPORTE', cod_dec, re.M)
    #print re.sub("^PRESUPUESTO Y MEDICIONES[\w\W]*IMPORTE", '', cod_dec, re.M)
'''
texto = re.sub("PRESUPUESTO Y MEDICIONES[\w\W]*?IMPORTE", '', texto)
texto = re.sub('Página *[0-9]{1,3}', '', texto)


texto_resumen = re.split('RESUMEN DE PRESUPUESTO',texto, re.M)[1]
texto_presupuesto = re.split('RESUMEN DE PRESUPUESTO',texto, re.M)[0]


buscCAP = re.compile(r'((TOTAL |)(CAPÍTULO|SUBCAPÍTULO|APARTADO|SUBAPARTADO)) ([0-9]{2}(\.[0-9]{2})*)',  re.M)
numero = '([0-9]{0,2}\.*[0-9]{0,3}\.*[0-9]{1,3},[0-9]{1,2})'


#print texto_presupuesto

#print re.search(buscCAP, texto_presupuesto[230000:]).group()

arbol = {}

texto_p = '''TOTAL CAPÍTULO 22 SEGURIDAD Y SALUD......................................................................................................  48.912,37'''


for capitulo in re.findall(buscCAP, texto_presupuesto):
    print capitulo[0], capitulo[3],
    try:
        if re.search('TOTAL',capitulo[0], re.M):
            cap_bus = capitulo[0]+ ' ' + capitulo[3] + '([\w\W]*?)\.* ?(' + numero + ')'
            print  '=', re.search(cap_bus, texto_presupuesto, re.M).group(2)
        else:
            pass
    except AttributeError:
        print 'Error'
numeros_texto = re.findall(numero, texto_presupuesto, re.M)

def convertir_num(texto):
    return re.split(',',re.sub('.','',texto))

print [convertir_num(nn)*1. for nn in numeros_texto]

busca = capitulo[0] + '[\w\W]* (' + numero + ') *\n'
busca = 'TOTAL CAPÍTULO 01' + '[\w\W]* (' + numero + ')'

#print re.search(busca, texto_presupuesto).group()
#print re.search(numero, texto_presupuesto).group()
#print re.search('([0-9]{0,2}\.*[0-9]{0,3}\.*[0-9]{1,3},[0-9]{1,2})','df 91.255,01')



if False:
    f = open('pres_limp.txt','w')
    f.write(texto_presupuesto)
    f.close()
