#Calcular la paga total de un trabajador
print('Calculando la paga de un trabajador \n\n');

#Entrada
nombre=input("Dame el nombre: ");
horasTrabajadas=int(input("Dame las horas trabajadas: "));
paga=float(input("Dame paga por hora: "));
tasa=0.3;

#Calculo
pagabruta= horasTrabajadas*paga;
impuesto=pagabruta*tasa;
pagaNeta=pagabruta-impuesto;

print(f"El trabajador {nombre}");
print(f"Paga bruta es: {pagabruta}");
print(f"Impuesto: {tasa}");
print(f"La paga neta es: {pagaNeta}");
