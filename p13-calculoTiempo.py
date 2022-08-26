#Dada una cantidad en horas, calcular su equivalente en días, minutos y segundos

horas=int(input("Ingrese la cantidad de horas: "));
dias=horas//24;
minutos=horas*60;
segundos=minutos*60;

print(f"La cantidad en dias es: {dias}");
print(f"La cantidad en minutos es: {minutos}");
print(f"La cantidad de segundos es: {segundos}");