#Capturar nombres y edades hasta introducir *

import os;
os.system("cls");

nombres=[];
edades=[];

print("Capturar nombres y edades hasta introducir *: ");

#introducir nombres y edadaes
while True:
    nombre=input("Ingresar Nombre: ");
    
    if nombre=='*':
        break;
    else:
        nombres.append(nombre);
        edad=int(input("Edad: "));
        edades.append(edad);

#imprimir nombres y edades
print();
print();
print(f"Nombres: {len(nombres)} - {nombres}");
print(f"Edades : {len(edades)} - {edades}");

#Recorrer el arreglo para ver los mayores de edad
for i in range(len(edades)):
    if edades[i]>=18:
        print(f"Nombre: {nombres[i]} - {edades[i]}");

#buscar alumno de mayor edad y mostar su nombre
mayor=max(edades);
pos=edades.index(mayor);

print(f"El nombre del alumno con mayor edad es: {nombres[pos]} - {edades[pos]}");
