#Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir 
#un mensaje de acuerdo al promedio obtenido: 
#• Entre 0 y 6 Quedas reprobado
#• Entre 6.1 a 7 Pasas de panzazo
#• Entre 7.1 y 8 Muy bien, pues mejorar
#• Entre 8.1 y 9 Excelente sigue así
#• Entre 91 y 10 Perfecto tu esfuerzo valió la pena}

print("ingrese 5 calificaciones:");
n1,n2,n3,n4,n5=input().split();
n1,n2,n3,n4,n5=float(n1),float(n2),float(n3),float(n4),float(n5);

promedio= (n1+n2+n3+n4+n5)/5.0;

print(f"El promedio que sacaste es de: {promedio}");

if promedio>=0 and promedio<=6:
    print("Quedas reprobado");
elif promedio>=6.1 and promedio<=7:
    print("Pasas de panzazo");
elif promedio>=7.1 and promedio<=8:
    print("Muy bien, pues mejorar");
elif promedio>=8.1 and promedio<=9:
    print("Exelente sigue asi");
elif promedio>=9.1 and promedio<=10:
    print("Perfecto tu esfuerzo valió la pena");