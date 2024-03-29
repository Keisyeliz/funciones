import os

def fnt_limpiarPantalla():
    os.system('cls')
    print('sistema de control de inventario')
    print('Autor: Keisy E. Murillo B. (c)- 2024')
    print('Universidad Católica Luis Amigó')
    print('\n\n')
    
def fnt_menu(repetir):
    while repetir == True:
        fnt_limpiarPantalla()
        
        opcionStr = input('---MENÚ DE OPCIONES---\n1. Sumar\n2. Restar\n3. Multiplicar\n4. dividir\n -> ')
        if  opcionStr == 'F' or opcionStr == 'f':
            repetir = False
        else:
            if int (opcionStr) >= 1 and int (opcionStr) <= 4 :
                numero1Flt = float(input('Ingrese el primer número -> '))
                numero2Flt = float(input('Ingrese el segundo número -> '))
                fnt_operaciones(numero1Flt,numero2Flt,opcionStr)
            else: 
                print('\n Opción incorrecta')
                enter = input('\n <ENTER>')
       
            
def fnt_operaciones(n1,n2,op):
    if op == '1':
        resultadoFlt = n1 + n2
        operadorStr = '+'
        
    if op == '':
        resultadoFlt = n1 - n2
        operadorStr = '-'
        
    if op == '3':
        resultadoFlt = n1 * n2
        operadorStr = 'x'
        
    if op == '4':
        if n2 == 0:
            enter = input('\n No se puede dividir por 0 <ENTER>')
        else:
            resultadoFlt = n1 / n2
            operadorStr = '/'
    print('\n',n1,' ',operadorStr,' ',n2,' = ',resultadoFlt)
    enter = input('\n <ENTER>')
        
fnt_menu(True)