#Imprime la secuencia de n armonicos y calcula su suma

print("Imprime la secuencia de n armonicos y calcula su suma");

n=int(input("Dame un número: "));
suma=0;

for i in range(1,n+1):
    if i==1:
        print("1+",end="");
        suma+=1;
    elif i==n:
        print(f"1/{i}",end="");
        suma+=(1/i);
    else:
        print(f"1/{i}",end="+");
        suma+=(1/i);
print(f"\nLa suma de los armonicos es: {suma}");
    