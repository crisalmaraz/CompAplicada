#El usuario ingresara la temperatura inicial y final en grados y la va convertira a farenheit
import os
while True:
    os.system("cls");
    ti=int(input("Ingrese la temperatura inicial en grados Centigrados: "));
    tf=int(input("Ingrese la temperatura inicial en grados Centigrados: "));

    contador=ti;
    while contador<=tf:
        farenheit=(contador*(9/5))+32;
        print(f"{contador}°C\t->\t{farenheit:.2f}°F");
        contador+=1;
    opc=input("Desea continuar (S/N): ").upper();
    if opc=='N':
        break;
