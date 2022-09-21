#Imprime la secuencia de n renglones con n veces

print("Imprime la secuencia de n renglones con n veces");

n=int(input("Dame un número: "));
for i in range(1,n+1):
    for x in range(1,i+1):
        print(x, end=" ");
    print();