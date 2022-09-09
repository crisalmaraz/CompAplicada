#Inprime la tabla de multiplicar deseada del 1 al 10
import os


while True:
    os.system("cls"); #borra la pantalla cls
    print("Imprime la tabla de multiplicar del 1 al 10");
    t= int(input("Que tabla quieres?: "));
    c=1;
    while c<=10:
        print(f"{c} x {t} = {c*t}");
        c+=1;
    res =input("Deseas continuar (S/N)?: ").upper();
    if res=='N':
        break