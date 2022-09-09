#Tabla de conversion de peso a dolar
# 10 a 20

while True:
    tc=19.91;
    tcl=23.00;
    print("Tabla de conversion de peso a dolar, libra");

    pi= float(input("Valor de pesos inicial : "));
    pf= float(input("Valor de pesos final   : "));

    c=pi;
    print("\nPeso\tDolar\tLibra");
    print('-'*15);
    while c<=pf:
        print(f"{c}\t {c/tc:.2f}\t{c/tcl:.4f}");
        c+=1;
    print('-'*15);
    res=input("Deseas continuar (S/N): ").upper();

    if res=='N':
        break;