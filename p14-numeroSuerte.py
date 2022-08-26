#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte. Mostrar los dígitos 
#individuales y el número de la suerte

anio=(input("Ingrese su año de nacimiento: "));

n1,n2,n3,n4= int(anio[0]),int(anio[1]),int(anio[2]),int(anio[3]);
numeroSuerte=n1+n2+n3+n4;
print(f"El primer digito es: {n4}");
print(f"El segundo digito es: {n3}");
print(f"El tercer digito es: {n2}");
print(f"El cuerto digito es: {n1}");
print(f"Tu número de la suerte es: {numeroSuerte}");