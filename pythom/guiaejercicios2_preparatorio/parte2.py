print ("bienvenido a nuestro sistema de apoyo de calculo de inversion porfavor ingrese los datos solicitados")
inv_inicial = int (input("inverison inicial solicitada = "))
tasa_de_descuento = float (input ("tasa de descueto = "))
tasa = (tasa_de_descuento) / 100 
i = 1 
Total = 0
MES = 0
VAN = float () 
while VAN <= 0  : 
    print ("porfavro ingrese el retorno esperado este mes", i )
    ingreso = int (input ())
    i = i + 1
    MES = (ingreso //(1 + tasa) ** i )
    Total = Total + MES 
    VAN = (- inv_inicial) + Total
    print("el retorno mensual es = ",MES)
    print ("el retorno acumulado es =",Total)
    print ("el VAN acual cubierto es = ",VAN) 
    
