
J = int (input(print ("ingrese la cantidad de variables a consultar")))
print ("recuerde que la variable a calcular sera aceptada entre los valores de  103  y 987")
i = 1 
Z = 0 
X = 0 
Y = 0
R = 0 
T = 0 
E = 0
rest1= 0 
rest2= 0
while  i <= J : 
    num = int ( input(print("ingrese el numero que desea invertir = ")))
    i = i + 1 
    if num >= 103 and num <= 987 : 
        Z = num // 10  
        X = Z//10 
        Y = X//10
        R = num%10
        T = Z%10
        E = X%10
        rest1 = R * 10 + T
        rest2= rest1 * 10 +  E 
        print ("la inversion de ", num,  "corresponde a = ", rest2)
    else : 
        print ("el numero", num ,"no es encuetra en los parametros de 103 y 987 solicitados")
