#Dado un dia de la semana, imprimir la paga correspondiente

import os;
os.system("cls");

print("Dado un dia de la semana imprimir la paga correspondiente");
dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
paga=[100,200,300,400,500,600,700];

print("Dado un dia de la semana, imprimir la paga correspondiente\n");

dia=input("Dame un dia de la semanacon letra: ");

if dia in dias:
    print("Si esta");
    print(f"Elegiste el dia {dia}");
    pos=dias.index(dia);
    print(pos);
    print(f"Le corresponde un pago de : {paga[pos]}");

else:
    print(f"No esta");