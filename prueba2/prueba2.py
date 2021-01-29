
"""
Prueba 2 para aplicación a Redsis
Autor: Juan Pablo Campos
Última modificación 29/01/2020
"""

import math

def encontrar_tripleta(num):
    #B puede estar entre 0 y el límite
    for b in range(num):
        #como a es más pequeño que b llega hasta b
        for a in range(1,b):
            c = math.sqrt(a**2 + b**2)
            
            #En caso tal de que c si me de un entero y la suma de los 3 sea 100 lo encontré
            if c.is_integer() and (a + b + c) == 1000:
                print(f"a:{a}, b:{b} ,c:{c}")
                print(f"a*b*c = {a*b*c}")


def main():
    encontrar_tripleta(1000)
    


if __name__ == '__main__':
    main()