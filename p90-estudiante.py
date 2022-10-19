#Diccionario con los datos de un estudiante

import os;
os.system("cls");

estudiante={
    "nombre":"Juan perez",
    "edad":45,
    "correo":"jperez@msn.com",
    "carrera":"Sistemas"
}

print(f"El diccionario: \n{len(estudiante)} - {estudiante}")

estudiante["calificacion"]=9.5;
estudiante["correo"]="jaunp@gmail.com";

print(f"El diccionario actualizado: \n{len(estudiante)} - {estudiante}")
print(f"\nLas llaves: \n{estudiante.keys()}\n");
for k in estudiante.keys():
    print(k);

print(f"\nLos valores: \n{estudiante.values()}\n");
for v in estudiante.values():
    print(v);

print("\nLlaves y valores:\n");
for k,v in estudiante.items():
    print(f"{k:<14} : {v}")