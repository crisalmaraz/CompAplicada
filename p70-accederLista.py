#Acceder a los elementos de una lista

import os;

os.system("cls");

print("Acceder a los elementos de una lista \n");
nums=[10,20,30,40,60,70,10,20,99];

print(f"Lista original      : {len(nums)} - {nums}");
print(f"Primero y el ultimo : {nums[0]} - {nums[8]}");
print(f"Del 2 al 6          : {nums[2:7]}");
print(f"Los primeros 3      : {nums[:3]}");
print(f"Los ultimos  3      : {nums[6:]}");
print(f"3 antes del ultimo  : {nums[5:8]} - {nums[-4:-1]}");

