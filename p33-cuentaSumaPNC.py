# Cuenta nùmeros ,la suma, cuenta : positivos, negativos y ceros, parar con 999

num=cuenta=suma=0;
cuenta_positivos=cuenta_negativos=cuenta_ceros=0;

print("Cuenta nùmeros ,la suma, cuenta : positivos, negativos y ceros, parar con 999");

while(True):
    num= int(input("Numero: "));
    if num!=999:
        cuenta+=1;
        suma+=num;
        if num>0:
            cuenta_positivos+=1;
        elif num<0:
            cuenta_negativos+=1;
        else:
            cuenta_ceros+=1;
    else:
        break

print(f"se introdujeron {cuenta} numeros");
print(f"La suma de los números es {suma}");
print(f"Positivos   : {cuenta_positivos}");
print(f"Negativos   : {cuenta_negativos}");
print(f"Ceros       : {cuenta_ceros}")
