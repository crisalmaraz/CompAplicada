#Formato datos, la nueva forma
import os;

os.system("clear");

noms="Juan Carlos Pedro Luis Jose Maria Julian Teresa Fransisco Leticia Rafael";
nombres=noms.split();
edad=25;
sueldo=12345.1234;
tasa=0.40;
print("\nSalida de datos con formato usando 'f'\n");

print(f"Nombre: {nombres[5]}, Edad: {edad}, Sueldo: {sueldo:,.2f}, Tasa: {tasa:.2%}");

print(f"\nNombres: {noms}");
print(f"\nNombres: {nombres}");

print(f"{'Tabla de datos':*^47}");
print(f"{'No':<6}{'Nombre':<15}{'Edad':^10}{'Sueldo':>15}");
print('-'*47);
for i in range(len(nombres)):
    print(f"{i:<6}{nombres[i]:<15}{edad+i:^10}{sueldo*i*5:>15,.2f}");