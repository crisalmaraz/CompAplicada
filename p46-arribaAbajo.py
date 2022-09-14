#imprime numeros de 1 a n o de n a 1 segun elija el usuario
import os;
while True:
    os.system("cls");
    print("imprime numeros de 1 a n o de n a 1 segun elija el usuario");
    print("[1] 1 a n");
    print("[2] n a 1");

    opc=int(input("Ingrese la opción: "));
    n=int(input("Limite de n: "));

    if opc==1:
        print(f"Imprimiendo números del 1 hasta {n}");
        for x in range(1, n+1, 1):
            print(x,end=" ");
    elif opc==2:
        print(f"Imprimiendo números del {n} hasta 1");
        for x in range(n, 0, -1):
            print(x,end=" ");
    else:
        print("opción incorrecta");
    w=input("\nDeseas continuar [S/N]").upper();
    if w=='N':
        break;
