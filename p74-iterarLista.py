#Iterar sobre los elementos de una lista
import os;

os.system("cls");
print("Iterar sobre los elementos de la lista\n");

nums=[2,4,6,8,10,12,14,16];
print(f"Lista original : {len(nums)} - {nums}\n");

print("\nIterar por los elementos de la lista");
for n in nums:
    print(n);

print("\nIterar por los elementos de la lista en base al indice");
for n in range(len(nums)):
    print(nums[n]);


print("\nIterar por los elementos de la lista");
for n in nums:
    print(n+2);

print("\nIterar por los elementos de la lista en base al indice");
for n in range(len(nums)):
    nums[n]+=2;
print(f"Lista modificada : {nums}");
