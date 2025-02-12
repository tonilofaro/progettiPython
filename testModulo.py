import miomulomodulo as em   # importo il modulo con unb alias
import platform as pt
import math
# from mazzo_carte import  VALORI    # importa solo una parte del modulo
import datetime

x = em.persona1['nome']
em.salta(x)
y = pt.system()
print(y)
print(math.factorial(5))
print(datetime.datetime.now().strftime("%d/%m/%Y")) # con strftime cambio formato
print(datetime.datetime(2012,3,19))


