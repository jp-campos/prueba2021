"""
Prueba 4 para aplicación a Redsis
Autor: Juan Pablo Campos
Última modificación 29/01/2020
"""
import os
        
        
class DiaSemana:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.sig = None
    
    def __str__(self):
        return self.dia


#Crea la lista circular y devuelve el objeto del primer día que entra como string en formato string
def init_semana(primerDia):
    dias = ['L','M','X','J','V','S','D']
    diasObj = [DiaSemana(d) for d in dias]
    
    diaRetorno = None
    for i in range(len(diasObj)):
        dia = diasObj[i]
        if dia.nombre == primerDia:
            diaRetorno = dia
        if i+1 < len(diasObj):
            dia.sig = diasObj[i+1]
        else:
            dia.sig = diasObj[0]
            
    
    return diaRetorno
        
    

def escribirMes(numMes,letra):
    
    #Encontrar cuantos días tiene el mes
    numDias =0 
    if numMes == 2:
        numDias = 29
    elif numMes < 7:
        numDias = 30 if numMes%2 == 0 else 31
    else:
        numDias = 31 if numMes%2 == 0 else 30
        
    diaSemActual = init_semana(letra).sig
    linea= '1'+letra
    
    for i in range(2,numDias+1):
        
        linea +=f"{i}{diaSemActual.nombre}" 
        diaSemActual = diaSemActual.sig
       
    #Guardar en un archivo
    rutaBase = os.path.dirname(__file__)
    nombreArchivo = f"mes{numMes}.txt"
    
    ruta = os.path.join(rutaBase,nombreArchivo)
    
    with open(ruta, 'w')as f :
        f.write(linea)
        
        
        
    
    

    
    
    
    
    

def main():
    
    print('Inserte el número')
    numMes = input()
    print('Inserte el día')
    diaSem = input()
    
    escribirMes(int(numMes), diaSem)



if __name__ == '__main__':
    main()