#Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 
#2 es lunes y así hasta 7 es viernes. Si el número no está en el rango especificado, mostrar un mensaje de error.

n=int(input("Ingrese el número de la semana: "));

if n==1:
    print("Domingo");
elif n==2:
    print("Lunes");
elif n==3:
    print("Martes");
elif n==4:
    print("Miercoles");
elif n==5:
    print("Jueves");
elif n==6:
    print("Viernes");
elif n==7:
    print("Sabado");
else:
    print("Número Invalido debe ser del 1 al 7");