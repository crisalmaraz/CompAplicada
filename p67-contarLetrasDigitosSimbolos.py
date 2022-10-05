#Modifique el programa p61 - contar letras, dígitos, símbolos, para que además de contar cuantas letras, dígitos
#y símbolos tiene una frase palabra, imprima cuales son estos

#Contar letras, digitos, simbolos

print("Contar letras, digitos, simbolos");

frase=input("Dame una frase: ");

let=dig=sin=0;
letras=digitos=simbolos="";

print(frase);
print(f"\nla frase tiene {len(frase)} caracteres");

for l in frase:
    if l.isalpha():
        let+=1;
        letras+=l;
    elif l.isdigit():
        dig+=1;
        digitos+=l;
    else:
        sin+=1;
        if l!=" ":
            simbolos+=l;
print(f"\nLetras: {let} - {letras} \nDigitos: {dig} - {digitos} \nSymbolos: {sin} - {simbolos}");