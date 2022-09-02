#Convertir de Farenheit a Centigrados y viceversa
print("Conversion de farenheit a centigrados y viceversa");
print(  "[C] convertir a centigrados");
print(  "[F] convertir a farenheit");

opcion=str.upper(input("Elige una opción: "));

if opcion=='C':
    print(  "Elegiste convertir a centigrados");
    temp=float(input("Dame los grados farenheit: "));
    res= (temp-32)*(5/9);
    print(  f"{temp} grados farenheit son {res:.2f} grados centigrados");
else:
    print(  "Elegiste convertir a farenheit");
    temp=float(input("Dame los grados centigrados: "));
    res= (temp*(9/5))+32;
    print(  f"{temp} grados centigrados son {res:.2f} grados farenheit");


