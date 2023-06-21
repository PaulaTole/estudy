Algoritmo hhols
	Definir i, num, suma Como Entero
	Definir op Como Caracter
	definir sigueSi, sigueNo  Como Logico
	definir prom Como Real
	i=1; 
	Suma = 0 ;
	prom = 0
	Repetir
		
	 
		mientras  i < 6 hacer 
		Escribir "ingrese su nota " , i , ":";
		leer num; 
			si num > 0
				i = i + 1; //contador 
				
				suma = suma + num; // acumulador 
				
				prom = suma / 5
			sino 
				escribir " el numrero debe ser positivo" 
			FinSi
		
		FinMientras
		
		escribir "Su pormedio es "  prom
		Escribir "deseas ingresar nuevamrntte (s/n)" 
		leer op
		si op = "s"  Entonces
			sigueSi = Verdadero
		sino op = "n" 
			sigueNo = falso 
		FinSi
	Hasta Que  op = "n"
FinAlgoritmo
