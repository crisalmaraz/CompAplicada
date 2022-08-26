#Calcular el volumen de un cilindro dado su radio y altura

import math

radio=float(input("Ingrese el valor del radio del cilindro: "));
altura=float(input("Ingrese el valor de la altura del cilindro: "));
volumen=math.pi*(radio*radio)*altura;
print(f"El volumen de cilindro es: {volumen:.2f}")