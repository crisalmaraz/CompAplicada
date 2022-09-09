# Imprime la conjetura de collatz
print("Imprime la conjetura de collatz");

num=int(input("Dame un número ?: "));

while num>1:
    print(num);
    if not num%2:
        num//=2;
    else:
        num=(num*3)+1;
print(num);