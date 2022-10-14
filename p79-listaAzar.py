#Generrar 2 listas de números aleatorios
import os;
import random;
os.system("cls");

l1=[];
l2=[];
l3=[];

print("Generando números aleatorios : ");
for n in range(10):
    l1.append(random.randint(1,10));
    l2.append(random.randint(1,10));

print("\nListas de números originales");
print(f"Lista 1: {l1}");
print(f"Lista 2: {l2}");

for n in range(10):
    l1[n]=pow(l1[n],2);
    l2[n]=pow(l2[n],2);
    l3.append(l1[n]+l2[n]);

print("\nListas de números procesadas");
print(f"Lista 1: {l1}");
print(f"Lista 2: {l2}");
print(f"Lista 3: {l3}");

