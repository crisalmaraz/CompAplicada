#Dividir un numero e tres cifras, en centenas de unidades
import math
num= int(input("Dame un número: "));
##math.trunc

centenas= num //100;
decenas = (num-centenas*100)//10;
unidades = (num-(centenas*100+decenas*10));
print(f"centenas {centenas}, decenas {decenas}, unidades {unidades}");