# Procesar un pedido de pizza

import os;
os.system("cls");

ingr={"T":1.50,"P":3.50,"C":3.74,"A":0.40};
base=15;
subtotal=0;
total=0;

pedio=input("Ingredientes [T]otame, [P]iña, [C]hampiñon, [A]guacate:\n").upper();

#precio=ingr["T"]+ingr["P"]+ingr["A"];

for i in pedio:
    if i in "TPCA":
        subtotal+=ingr[i];
subtotal=subtotal+15;

if subtotal>=20:
    total=subtotal-(subtotal*0.05);

print(f"Subtotal sin descuento: {subtotal}");
print(f"El total con descuento: {total}");