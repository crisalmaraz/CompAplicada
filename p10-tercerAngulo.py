#programa para calcular dados dos ángulos de un triángulo, calcular el 3er ángulo

lado1=float(input("Ingrese la medida del primer lado: "));
lado2=float(input("Ingrese la medida del segundo lado: "));
angulo3= 180-(lado1+lado2);
print(f"La medida del tercer ángulo: {angulo3:.2f}");