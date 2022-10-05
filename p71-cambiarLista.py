# Cambiar los elementos de una lista

import os;
os.system("cls");

print("Cambiar los elementos de una lista\n");
nums=[10,9,8.5,6.5,9.8,7,5,6.2,9.5];

print(f"Lista original: {len(nums)} - {nums}\n");
nums[0]=7;
nums[1]=7;
print(f"Cambiar 0 y 1 : {nums} \n");

nums[2:5]=[9,9,9];
print(f"Cambiar del 2 al 4 : {nums}\n");