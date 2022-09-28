#Contar vocales y consonantes

frase ='''Al año los murcielagos huyen de la fuerte luz que \
    bsjs por el kiosko de wivex''';

voc=0;
con=0;
otr=0;

print(frase);
print(f"La frase tiene {len(frase)} caracteres");

for letra in frase:
    if letra.isalpha():
        if letra in "aeiouAEIOU":
            voc+=1;
        else:
            con+=1;
    else:
        otr+=1;

print(f"vocales: {voc}");
print(f"consonantes: {con}");
print(f"otras: {otr}");