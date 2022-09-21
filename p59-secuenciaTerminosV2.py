#Imprime la secuencia de n armonicos y calcula su suma

print("Imprime la secuencia de n armonicos y calcula su suma");

n=int(input("Dame un número: "));
sum="";
suma=0;

for i in range(1,n+1):
    for x in range(1,i+1):
        print("1",end="");
        sum+="1";
    suma+=int(sum);
    sum="";
    if x!=n:
        print("+",end="");
print(f"\nLa suma de los términos es: {suma}");