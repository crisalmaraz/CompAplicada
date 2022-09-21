#Imprime la tabla de multiplicar, hasta donde se pida
import os;

while True:
    os.system("cls");
    print("Imprime la tabla de multiplicar, hasta donde se pida");

    t= int(input("Que tabla quieres: "));
    n= int(input("Hasta donde va a ser la tabla: "));

    for i in range(1,n+1):
        print(t,"x",i,"=",t*i);
    opc=input("Deseas continuar (S/N): ").upper();
    if(opc=='N'):
        break;