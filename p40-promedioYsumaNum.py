# Calcula la suma y promedio de los números ingresados, presione 0 para terminar

num=cuenta=suma=0;

print("Calcula la suma y promedio de los números ingresados, presione 0 para terminar");

while(True):
    num= int(input("Numero: "));
    if num!=0:
        cuenta+=1;
        suma+=num;
    else:
        break

print(f"La suma de los números es {suma}");
print(f"El promedio de los números es: {suma/cuenta:.2f}");