# Agregar elementos a una lista existente

import os;
os.system("cls");

print("Agregar elementos a una lista existente");

nums=[80.3,12.5,60.2,30.4];
print(f"Lista original : {len(nums)} - {nums} ");

nums.append(90);
nums.append(100);
print(f"Agregar 90 y 100 al final : {len(nums)} - {nums}")

nums.insert(4,80);
print(f"Insertar el 80 antes del 90 : {nums}")

otros=[110,120,130];
nums.extend(otros);
print(f"extender 110 120 y 130 {nums}");

nums.extend([5,6,7]);
print(f"extender 5 6 y 7 {nums}");