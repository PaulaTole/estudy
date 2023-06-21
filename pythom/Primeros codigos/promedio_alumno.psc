Algoritmo promedio_alumno 
	Definir i, num, suma Como Entero ;
	definir prom Como Real ;
	
	i = 1 ;
	suma = 0 ; 
	mientras  i < 4 hacer 
		Escribir "ingrese su nota " , i , ":";
		leer num; 
		si num > 9 y num < 71 Entonces
			
			i = i + 1; 
			
			suma = suma + num;  
			
			
		sino 
			escribir " el numrero debe ser positivo" ;  
		FinSi
		
	FinMientras
		prom = suma / 3 ;
	escribir "Su pormedio es " , prom ; 
	
FinAlgoritmo
