#Número pares descendente

while True:
    n=int(input("Hasta que número va a imprimir: "));
    c=100;
    suma=0;
    while c>=n:
        if c%2==0:
            print(f"{c}");
            suma+=c;
        c-=1;
    print(f"La suma de los números es: {suma}");
    opc=input("Desea continuar (S/N): ").upper();
    if opc=='N':
        break;