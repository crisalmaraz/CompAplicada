#Imprime la tabla de multiplicar hasta n tablas
import os;

while True:
    os.system("cls");
    print("Imprime la tabla de multiplicar hasta n tablas");

    n=int(input("Hasta que tabla va a ser: "));
    k=int(input("Hasta que número va a ser: "));

    for i in range(1,n+1):
        for j in range(1,k+1):
            print(i,"x",j,"=",i*j);
        print("----------------");
    opc=input("Deseas continuar (S/N): ").upper();
    if(opc=='N'):
        break;