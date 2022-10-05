# Modifique el programa p60 - vocales, consonantes , para que además de contar cuantas vocales y consonantes 
# tiene una frase, imprima cuales son estas. (ver también p62)

#Contar vocales y consonantes
frase ='''El dia se pasa muy rapido''';

voc=0;
vocales="";
con=0;
consonantes="";

print("Frase: {frase}");

for letra in frase:
    if letra.isalpha():
        if letra in "aeiouAEIOU":
            voc+=1;
            vocales+=letra;
        else:
            con+=1;
            consonantes+=letra;


print(f"vocales: {voc} - {vocales}");
print(f"consonantes: {con} - {consonantes}");