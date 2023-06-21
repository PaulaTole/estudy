while True :
    print (" bienvendio a nuestro sistema de solicitud de credtios ,por favro ingrese los siguietnes datos para  confirmar si usted es apto para realizar la solicitud")
    monto= int (input (print ("porfavro ingrese el monto del cual solcitada este credito y porfavor recierte que el monto no puede ser infeior a $500.0000")))
    if monto >= 500000 : 
        print ("porfavor ingrese las cuotas a las que desea que se pagara este credito, recuerde que los plazos son de 3  a  84 cuotas")
        cuota = int (input())
        if cuota >= 3 and cuota <= 84 : 
            print ("porfaovr ingrese su edad y reuerde que los rangos de edad aceptabeols son entre 24 y 79 años")
            edad = int (input())
            if edad >= 24 and edad <= 79 : 
                print ("espere muentras hacemos comprovacion")
                if edad + cuota <= 102 : 
                    print  ("muchas gracias por esperar")
                    print ("porfavor ingrese su nacionalidad")
                    nacion = input ()
                    nacionalidad = nacion.lear 
                    if nacionalidad == "Chilena" : 
                        print ("")
                if edad + cuota > 102 : 
                        print ("disculpe pero los datos ingresados no son coerentes pofavor espere")