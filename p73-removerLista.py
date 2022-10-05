# Remover elementos de una lista existente
import os; 
os.system("cls");

print("Remover elementos de una lista existente\n");

nums=[1,3,5,7,9,11,99,15,88,19,100];
print(f"Lista completa: {len(nums)} - {nums} \n");

nums.remove(99);
print(f"Remover el 99 la primera ocurrencia: {nums}\n");

num=nums.pop(8);
print(f"Remover elemento de una posición 8: {nums} - {num}\n");

num=nums.pop();
print(f"Remover elemento de una posición 8: {nums} - {num}\n");

nums.clear();
print(f"Remover todos: {nums}\n");
