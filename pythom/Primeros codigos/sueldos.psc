Proceso sueldos
	Definir empleado, num , sueldo, tiempo Como Entero;
	definir resulado Como real;
	Escribir " ingrese numero de empleado" ;
	Leer empleado ;
	resulado = 0; 
	tiempo = 0 ; 
	mientras  tiempo < 4 hacer 
		Escribir "ingrese anos de servicio " , empleado , ":";
		leer tiempo; 
		si tiempo > 4 y tiempo < 11 Entonces
			Escribir " ingrese sueldo" ;
			leer sueldo ;
			
			empleado = empleado + 1; 
			
			Resulado = sueldo * 0.15 ; 
			
			
			si timepo >10 y tiempo < 21 entonces 
				Escribir " ingrese sueldo";
				leer sueldo ;
			empleado = empleado + 1;
			
			Resultado = sueldo + 0.20;
		FinSi
		
		si  tiempo > 21 entonces
			escribir "ingrese sueldo" ; 
			Leer sueldo ;
			
				empleado = empleado + 1 ;
				
				resultado = Sueldo + 0.25 ;
			sino 
				Escribir  " el empleado no necesita reajuste" ;
			FinSi
		
		FinSi
		
	FinMientras 
	escribir  resultado ;
FinProceso
