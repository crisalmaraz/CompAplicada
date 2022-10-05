#El usuario introduce dos palabras con igual número de caracteres (validar que así sea), se crea una palabra 
#combinada con las dos donde se toma 1 carácter de la primera y 1 carácter de la segunda hasta terminar ambas 
#palabras, además mostrar el número de caracteres de las palabras

palabra1=input("Ingrese una palabra : ");
palabra2=input("Ingrese otra palabra: ");

suma="";
if len(palabra1)==len(palabra2):
    for i in range(len(palabra1)):
        suma+=palabra1[i];
        suma+=palabra2[i];
    print(f"Palabra 1 : {palabra1}");
    print(f"Palabra 2 : {palabra2}");
    print(f"Combinadas: {suma}");

else:
    print("Las palabras son de distinto tamaño!!");
    print(f"    La palabra {palabra1} tien {len(palabra1)} caracteres.");
    print(f"    La palabra {palabra2} tien {len(palabra2)} caracteres.");
