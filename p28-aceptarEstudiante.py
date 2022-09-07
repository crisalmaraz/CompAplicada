#Dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones, decidir si el estudiante es aceptado. La 
#Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5

nombre=input("Ingresa tu nombre: ");
sexo=input("Ingresa tu sexo (h/m): ").upper();
edad=int(input("Ingresa tu edad: "));
print("Ingresa 3 calificaciones: ");
n1,n2,n3=input().split();
n1,n2,n3=float(n1),float(n2),float(n3);

promedio=(n1+n2+n3)/3.0;
if sexo=='M' and edad>21 and promedio>=8 and promedio<=9.5:
    print(f"Felicidades {nombre} has sido aceptado en la universidad Kitty Kat SA");
else:
    print(f"{nombre} no has sido aceptado, Universidad Kitty Kat SA es solo para mujeres mayores de 21 años con un promedio de entre 8 y 9.5");