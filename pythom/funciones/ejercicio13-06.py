import funciones as fn 
op= 3

while op != 4 :
    print ("1. calcular iva")
    print ("2. descuento")
    print ("3. clcular IMC")
    print ("4. salir")
    op = int (input("ingrese su opcion: "))

    if op == 1 : 
        precio = int (input("ingrese el precio del producto: "))
        iva = fn.calculoIVA(precio) 
        print ("iva =", iva)
    else : 
        if op == 2 :
            precio = int (input("ingrese el precio del producto: "))
            descuento = float (input("ingrese tasas de descuento"))
            preciofinal= fn.descuento(precio,descuento)
            print ("el precio final es : ", preciofinal)