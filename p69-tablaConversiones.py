#El usuario introduce un rango de números, luego se le muestra una tabla de conversiones con 4 columnas 
#alineadas: 1 numero decimal en alineación izquierda, 2 número hexadecimal en alineación centrada, 3 número 
#octal en alineación izquierda, 4 binario en alineación derecha, el tamaño de cada columna debe ser uniforme y el 
#título de la tabla debe centrarse en el ancho de la tabla

inicio=int(input("Inicio: "));
fin=int(input("fin: "));

print(f"{'Tabla de conversiones':^40}");
print(f"{'':-^40}");
print(f"{'...Decimal,,,Hexa,,,Octal.....,,,Binario'}");
print(f"{'':-^40}");
for i in range(inicio,fin+1,1):
    print(f"{i:>10}{i:^10x}{i:<10o}{i:>10b}");
