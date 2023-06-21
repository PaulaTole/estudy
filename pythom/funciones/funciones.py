def saludo(nombre):
    print("hola",nombre)
    print("Bienvenido a este mágico lenguaje de programación")

def calcularEdad(añoNac):
    añoActual = 2023
    edad = añoActual - añoNac
    print("Ud tiene ",edad, " años app")

def sumar(num1, num2 ) :
    suma = num1 + num2
    return suma 

def calculo (precio, descuento): 
    return precio - (precio * descuento/100)
    
    #datos = (10000, 10)

    #print ("el monto a pagar es: ", calculo (*datos))

def calculoIVA (iva, precio):
    iva = precio * 0.19 
    return iva
def descuento (precio,descuento):
    preciofinal = precio - (precio*descuento/100)
