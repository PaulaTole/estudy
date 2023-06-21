print ("bienvenido")

payasos= 300 
muñeca = 450 
paquetes= int (input("ingrese a la cantidad de paquetes enviados en el periodo ="))
i= 0
i1= 0 
i2 = 0 
i3 = 0 
i4 = 0
i5 = 0 
i6 = 0
precio =  0
total = 0
cantidad1=0 
cantidad2=0 
cantidad3=0 
cantidad4=0  
cantidad5=0 
cantidad6=0 
while i < paquetes : 

        cant1 = int(input("por favor ingrese al cantidad de muñecas vendidas en este paquete = " )) 
        cant2 = int(input("por favor ingrese al cantidad de payasos vendidos en este paquete ="))     
        try:
            if payasos*cant2 + muñeca * cant2 <= 1000 :
                    print ("porfavo confirme al zona a  la  que se envia el paquete, ya sea {zona norte}, {zona centro} o {zona sur} ")
                    precio =  input ()
                    
                    try:
                        if  precio == "zona norte" :
                             
                            cantidad1 = 3000
                            print ("el valor de este paquete es de", cantidad1)
                            i1 = i1 + 1 
                        if precio == "zona centro" : 
                            
                            cantidad2 = 2000 
                            print ("el valor de este paquete es de", cantidad2)
                            i2 =  i2 + 1
                        if precio == "zona sur" : 
                            
                            cantidad3 = 4000
                            print ("el valor de este paquete es de", cantidad3)
                            i3 = i3 + 1
                    except : 
                        print ("ingreso erroneo") 
            if payasos*cant2 + muñeca * cant2 >  1000 : 
                    print ("porfavro confirme al zona a  la  que se envia el paquete ya sea {zona norte}, {zona centro} o {zona sur} ")
                    precio = input ()
                    try:
                        if  precio == "zona norte" :
                             
                            cantidad4 = 5000
                            print ("el valor de este paquete es de", cantidad4)
                            i4 = i4 + 1
                        if precio == "zona centro" : 
                             
                            cantidad5 = 3000 
                            print ("el valor de este paquete es de", cantidad5)
                            i5 = i5 + 1 
                        if precio == "zona sur" : 
                            
                            cantidad6 = 7000
                            print ("el valor de este paquete es de", cantidad6)
                            i6 = i6 + 1
                    except: 
                        print ("ingreso erroneo")
        except : 
            print ("error de intgreso")
        i = i + 1
        total = i1 * cantidad1 + i2 * cantidad2 + i3 * cantidad3 + i4 * cantidad4 + i5 * cantidad5 + i6 * cantidad6 

        print ("el valor total de lo facturado en el periodo es ", total)