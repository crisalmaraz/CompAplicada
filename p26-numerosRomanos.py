#Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V, 
#VI, VII, VIII, IX, X). Si el número no esta en el rango solicitado que mande un mensaje de error

n=int(input("Ingrese un número del 1 al 10: "));

if n==1:
    print("I");
elif n==2:
    print("II");
elif n==3:
    print("III");
elif n==4:
    print("IV");
elif n==5:
    print("V");
elif n==6:
    print("VI");
elif n==7:
    print("VII");
elif n==8:
    print("VIII");
elif n==9:
    print("IX");
elif n==10:
    print("X");
else:
    print("Número Invalido debe ser del 1 al 10");