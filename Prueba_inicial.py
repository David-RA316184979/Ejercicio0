import fileinput

#Suncion de suma
def suma(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

def main():
    #Para leer el archivo
    numeros = []
    for line in fileinput.input():
        numeros.append(line)
    suma(numeros)
    print(suma)


