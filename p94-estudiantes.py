#Una lista donde cada elemento es un diccionario

import os;
os.system("cls");

grupo = [
    {'nombre':'Carlos','edad':45,'carrera':'sistemas','promedio':9} ,
    {'nombre':'Rocio','edad':35,'carrera':'sistemas','promedio':10}
];

print(f'Grupo original {grupo}');
n = int(input("Cuantos estudiantes deseas procesar: "));

for i in range(n):
    print(f'\nEstudiante {i+1}');
    datos = {};
    datos['nombre'] = input('Nombre: ');
    datos['edad'] = int(input('Edad: '));
    datos['carrera'] = input('Carrera: ');
    datos['promedio'] = float(input('Promedio: '));
    grupo.append(datos)

print(f'Grupo completo: {grupo}');
print(f'\nLos nombres de los estudiantes en el grupo: \n');

for e in grupo:
    for k,v in e.items():
        print(f'{k:<10} : {v}')
    print('')