#Imprime un rectangulo de n filas por c columnas
import os;

while True:
    os.system("cls");
    print("Imprime un caracter en n filas por c columnas");

    n=int(input("Cuantas filas van a ser: "));
    c=int(input("Cuantas columnas van a ser: "));
    caracter=input("Que caracter se va a imprimir: ");

    for i in range(1,n+1):
        for j in range(1,c+1):
            print(caracter, end='');
        print();
    opc=input("Deseas continuar (S/N): ").upper();
    if(opc=='N'):
        break;