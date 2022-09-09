#Inprime la tabla de multiplicar deseada del 1 a n
import os


while True:
    os.system("cls"); #borra la pantalla cls
    print("Imprime la tabla de multiplicar del 1 al 10");
    t= int(input("Que tabla quieres?: "));
    n= int(input("Hasta donde quieres que llegue?: "));
    c=1;
    while c<=n:
        print(f"{c} x {t} = {c*t}");
        c+=1;
    res =input("Deseas continuar (S/N)?: ").upper();
    if res=='N':
        break