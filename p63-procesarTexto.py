#Procesar texto
import os;

txt='''Aprender a programar Python es una tarea \
    que requiere tiempo y constancia la practica esta \
    en la experiencia'''

os.system("clear");
print(f"Texto: {len(txt)} - {txt}");

pal = input("Dame una palabra: ");
pos=txt.find(pal);

if pos!=-1:
    print(f"La palabra {pal} fue encontrada");
    if txt.startswith(pal):
        print(f"La palabra {pal} esta al inicio del texto");
    elif txt.endswith(pal):
        print(f"La palabra {pal} esta al final del texto");
    else:
        print(f"La palabra: {pal} aparece en: {pos}");
        print(f"La palabra: {pal} aparece en: {txt.count()} veces");
        txt2=txt.replace(pal, pal.upper());
        print(f"Texto modificado: {txt2}");
else:
        print(f"La palabra {pal} No fue encontrada");    

print(f"\nProcesamiento de texto");
print(f"Mayusculas : {txt.upper()} \n");
print(f"Minusculas : {txt.lower()} \n");
print(f"Titulo     : {txt.title()} \n");

txt3=txt.split();
print(f"\nSeparar: {txt3}");
##print(f"\nUnir: {",".join(txt3)}");