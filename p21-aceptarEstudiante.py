#Aceptar a un estudiante de acuerdo a ciertos criterios

print("Aceptar un estudiante de acuerdo a ciertos criterios");

nombre=input("Dame tu nombre: ");
edad=int(input("Dame tu edad: "));

if edad==18:
    print("Dame 2 calificaciones: ");
    c1,c2=int(input()), int(input());

    if c1>=8 and c2>=8:
        print(f"{nombre} bienvenido a la universidad Patria, tu edad es {edad} y tus calificaciones son {c1} y {c2}");
    else:
        print("No aceptamos calificaciones menores a 8, lo sentimos");
else:
    print("No aceptamos menores de edad, lo sentimos");
