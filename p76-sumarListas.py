#Sumar 2 listas de n números en una tercer lista

import os;
os.system("cls");

print("Sumar 2 listas de n números en una tercer lista \n");
c=int(input("Cuantos elementos van a ser: "));

#leer lista 1
lista1=[];
print("--Leyendo elementos de la lista 1--");
for i in range(c):
    n=int(input(f"introducir número {i}: "));
    lista1.append(n);

#leer lista 2
lista2=[];
print("--Leyendo elementos de la lista 2--");
for i in range(c):
    n=int(input(f"introducir número {i}: "));
    lista2.append(n);

#calcular suma y almacenar
lista3=[];
for i in range(c):
    lista3.append(lista1[i]+lista2[i]);

#mostrar las 3 listas
print(f"La lista 1 es           : {lista1}");
print(f"La lista 2 es           : {lista2}");
print(f"La suma de las listas es: {lista3}");
