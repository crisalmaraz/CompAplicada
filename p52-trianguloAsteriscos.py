#Imprime una piramide de asteriscos
import os;

while True:
    os.system("cls");
    print("Imprime asteriscos en n lineas");

    n=int(input("Cantos renglones van a ser: "));
    c=input("Que caracter va  ir: ");

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(c, end='');
        print();
    opc=input("Deseas continuar (S/N): ").upper();
    if(opc=='N'):
        break;