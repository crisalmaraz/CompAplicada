#Crear un diccionario de materias y calificaciones en base a dos listas

import os;
os.system("cls");

materias=["Fisica","Quimica","Matematicas","Geografia","Estadistica"];
califs=[10,9,8,7.5,6];

print(f"Listas de materias: \n{materias}");
print(f"Lista de calificaciones: \n{califs}")

notas=dict(zip(materias,califs));

print(f"\nDiccionario de notas: \n {len(notas)} - {notas} ");
notas.update({'Ingles':10});
notas.update({'Programacion':7});
print(f"\nSe agregaron elementos : \n{len(notas)} - {notas}");

notas.update({'Quimica':10});
notas['Matematicas']=10;7
print(f"\nSe modificaron elementos : \n{len(notas)} - {notas}");

s=0
print('\nMaterias y calificaciones');
for m,c in notas.items():
    print(f'{m:<12} - {c:5}')
    s+=c
p=s/len(notas)
print(f'\nLa suma: {s} y el promedio: {p}')
notas.clear()
print(f'\nSe borro todo : {notas}')