# Procesar n calificaciones introducidas por el usuario
import os;

os.system("cls");
print("Procesar n calificaciones introducidas por el usuario");
print("Introduce calificaciones 0..10, usa 99 para parar");

n=0;
nums=[];
suma=0;

while n!=99:
    n=int(input("Numero: "));
    if n>=0 and n<=10:
        nums.append(n);
        suma+=n;
    else:
        print("x");

prom=suma/len(nums);
mp=[];

for num in nums:
    if num>prom:
        mp.append(num);
print(f"Calificaciones      : {len(nums)} - {nums}");
print(f"La suma es          : {suma}");
print(f"El promedio es      : {prom}");
print(f"Mayores al promedio : {len(mp)} - {mp}");
print(f"El mayor es         : {max(nums)}");
print(f"El menor es         : {min(nums)}");