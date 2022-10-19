# Listas multiplica

import os;
os.system("cls");

print("Leer 2 listas de 5 elemtos \n");

#leer lista 1
lista1=[];
print("--Leyendo elementos de la lista 1--");
for i in range(5):
    n=int(input(f"introducir número {i}: "));
    lista1.append(n);

#leer lista 2
lista2=[];
print("--Leyendo elementos de la lista 2--");
for i in range(5):
    n=int(input(f"introducir número {i}: "));
    lista2.append(n);

#calcular multiplicaciòn y almacenar
lista3=[];
for i in range(5):
    lista3.append(lista1[i]*lista2[i]);

#mostrar las 3 listas
print(f"La lista 1 es           : {lista1}");
print(f"La lista 2 es           : {lista2}");
print(f"La multiplicaciòn de las listas es: {lista3}");
