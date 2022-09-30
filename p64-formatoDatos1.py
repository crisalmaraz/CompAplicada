#Cadenas de formato

import os
os.system("cls");

ciudad0="Zacatecas";
ciudad1="Guadalupe";
ciudad2="Fresnillo";

print("\nSalida con argumentos por posición");
print("Posición numerada en orden: {0} {1} {2}".format(ciudad0,ciudad1,ciudad2));
print("Posición sin número: {0} {1} {2}".format(ciudad0,ciudad1,ciudad2));
print("Posición numerada sin orden: {2} {1} {0}".format(ciudad0,ciudad1,ciudad2));
print("Repetir posición: {2} {2} - {1} {1} - {0}".format(ciudad0,ciudad1,ciudad2));
print("\nArgumentos por nombre: {x1} / {x2} / {x3}".format(x1=4,x2=5,x3="Prueba"));

txt="Maestria en Ingenieria y Tecnologia Aplicada";
print("\nAlinear texto y especificar longitud\n");
print("{:*^50}".format(txt));
print("{:>60}".format(txt));
print("{:<60}".format(txt));

num=12345;
print("\nMostrar numeros en diferentes bases");
print("Decimal              :{:d}".format(num));
print("Hexadecimal 0-9 A-F  :{:x}".format(num));
print("Octal 0-8            :{:o}".format(num));
print("Binario 0,1          :{:b}".format(num));

num=1234.56789;
desc=0.20;

print("\n\nFormateo de numeros \n");
print("Numero decimal       : {:15}".format(num));
print("Con decimales        : {:.2f}".format(num));
print("Relleno              : {:15.2f}".format(num));
print("Exponencial          : {:e}".format(num));
print("En porcentaje        : {:.2%}".format(0.20));
print("En porcentaje        : {:,.2f}".format(num));