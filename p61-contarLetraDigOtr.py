#Contar letras, digitos, simbolos

print("Contar letras, digitos, simbolos");

frase=input("Dame una frase: ");

let=dig=sin=0;

print(frase);
print(f"\nla frase tiene {len(frase)} caracteres");

for l in frase:
    if l.isalpha():
        let+=1;
    elif l.isdigit():
        dig+=1;
    else:
        sin+=1;
print(f"\nLetras: {let} \nDigitos: {dig} \nSymbolos: {sin}");