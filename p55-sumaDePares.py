#Imprime los números de 2 a n y su suma

print("Imprime los números de 2 a n y su suma");

n=int(input("Dame un número: "));
suma=0;
for i in range(2,n+1,2):
    print(i, end=" ");
    suma+=i;
print(f"\nLa suma de los pares es: {suma}");
