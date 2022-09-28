#Dividir una frase en palabras y contar consonantes y vocales

print("Dividir una frase en palabras y contar consonantes y vocales");

frase ='''Al año los murcielagos huyen de la fuerte luz que \
    baja por el kiosko de wivex''';

print(f"{len(frase)} - {frase} \n");

palabras=frase.split();

print(f"{'Divición de palabras':-^35}")
for palabra in palabras:
    voc=0;
    con=0;
    otr=0;

    print(f"{len(palabra):>4} - {palabra:<12}", end="");

    for letra in palabra:
        if letra in "aeiouAEIOU":
            voc+=1;
        else:
            con+=1;

    print(f" - v:{voc:>4} - :{con:>4}");
print(f"{'Final':-^35}");