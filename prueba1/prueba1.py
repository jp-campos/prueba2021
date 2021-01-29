
"""
Prueba 1 para aplicación a Redsis
Autor: Juan Pablo Campos
Última modificación 29/01/2020
"""

import os

#Función encargada de leer el archivo con las tuplas de letras y números y retornar un diccionario 
#correspondiente
def lectura_diccionario(ruta):
    dicc = {}
    with open(ruta ) as f:
        for l in f.readlines():
            partes = l.split('=')
            num = partes[0].strip()
            letra = partes[1].strip()
            dicc[num] = letra
            
    return dicc

#Función que recorre la entrada y consigue la traducción del diccionario creado
def traduccion(cadena, dicc):
    ret = ''
    for letra in cadena:
        charTrad = dicc[letra]
        ret+= charTrad
    
    return ret

def main(cadena):
    rutaBase = os.path.dirname(__file__)
    nombreArchivo = 'paramsTraduccion.txt'
    ruta = os.path.join(rutaBase, nombreArchivo )
    
        
    dicc = lectura_diccionario(ruta)
    cadenaTrad = traduccion(cadena, dicc)
    
    print(cadenaTrad)
    
        


if __name__ == '__main__':
    print('Inserte el código a traducir')
    inputStr = input()
    if len(inputStr) != 10:
        raise Exception('Inserte una cadena de 10 dígitos por favor')
    else:
        main(inputStr)

