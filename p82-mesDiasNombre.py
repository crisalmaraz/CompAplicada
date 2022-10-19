#mes dias y nombre

import os;
os.system("cls");

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
dias=[31,28,31,30,31,30,31,31,30,30,31,30];
n=int(input("Ingrese el número del mes: "));

print(f"{meses[n-1]},{dias[n-1]}");