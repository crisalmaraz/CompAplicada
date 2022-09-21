#Números de 10 en 10 hasta n


print("Números de 10 en 10 hasta n");

n=int(input("Dame un número: "));

for i in range(1,n+1,10):
    print(i, end=" ");