#imprime el factorial de un nùmero

print("imprime el factorial de un nùmero");

n=int(input("Dame un nùmero entero: "));
factorial=1;

for x in range(1,n+1,1):
    print(x, end="x");
    factorial*=x;

print(f"\nEl factorial de {n} es: {factorial}");