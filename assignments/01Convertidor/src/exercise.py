# Escribe tus funciones abajo de esta línea
def pies_cm(pies):
    piescm=pies*30.48
    return piescm
def pulgadas_cm(pulgadas):
    pulgadascm=pulgadas*2.54
    return pulgadascm
def yardas_cm(yardas):
    yardascm=yardas*91.44
    return yardascm
def main():
    print ('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    convertir=int(input('Introduce una opcion: '))
    cantidad=int(input('Introduce la cantidad: '))
    if cantidad>0:
        if convertir==1:
            print(pies_cm(cantidad))
        elif convertir==2:
            print(pulgadas_cm(cantidad))
        elif convertir==3:
            print(yardas_cm(cantidad))
        else:
            print('Error')
    else:
        print('Error')
    
    # Escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
