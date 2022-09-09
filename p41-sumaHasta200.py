# Calcula la suma hasta que llegue a 200 o mas, el proceso se repetira hasta que el usuario lo quiera

while True:
    print("Calcula la suma hasta que llegue a 200 o mas, el proceso se repetira hasta que el usuario lo quiera");
    num=cuenta=suma=0;
    while True:
        if suma<200:
            num= int(input("Numero: "));
            cuenta+=1;
            suma+=num;
        else:
            break

    print(f"Se introdujeron {cuenta} números");
    print(f"La suma de los números es {suma}");
    opc=input("Desea continuar (S/N): ").upper();
    if opc=='N':
        break;
