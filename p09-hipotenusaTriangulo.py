#Programa para calcular la hipotenusa de un triangulo rectangulo
import math

a=float(input("Ingrese la medida del lado a: "));
b=float(input("Ingrese la medida del lado b: "));
hipotenusa= math.sqrt((a*a)+(b*b));
print(f"La hipotenusa es: {hipotenusa:.2f}");