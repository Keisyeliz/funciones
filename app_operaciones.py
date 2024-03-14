import os

def fnt_calcular(distancia,tiempo):
    global velocidad
    velocidad = distancia/tiempo
    
def fnt_mensaje(msn):
    print(msn, ' ',velocidad,'km')
    

fnt_calcular(150,5)
fnt_mensaje('La velocidad promedio equivale a:')