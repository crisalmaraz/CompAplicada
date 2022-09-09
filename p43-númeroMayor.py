## Calcula el número mayor presione 0 para terminar

print("Calcula el número mayor presione 0 para terminar");

mayor=0;

while(True):
    num= int(input("Numero: "));
    if num!=0:
        if num>mayor:
            mayor=num;        
    else:
        break

print(f"El número mayor es {mayor}");