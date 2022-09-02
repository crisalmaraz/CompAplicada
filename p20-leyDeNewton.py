# segunda ley de newton fuerza = masa por aceleraciòn

print("Calcular los valoes de la segunda ley de newton");
print("[F] fuerza       f=m*a");
print("[M] masa         m=f/a");
print("[A] aceleración  a=f/m");

op= str.upper(input("Elige una opción: "));
if op=='F':
    print("Calculando la fuerza");
    m=int(input("Dame la masa: "));
    a=int(input("Dame la aceleración: "));
    f=m*a;
    print(f"La fuerza es {f}");
elif op=='M':
    print("Calculando la masa");
    f=int(input("Dame la fuerza: "));
    a=int(input("Dame la aceleración: "));
    m=f/a;
    print(f"La masa es {m}");
elif op=='A':
    print("Calculando la aceleración");
    f=int(input("Dame la fuerza: "));
    m=int(input("Dame la masa: "));
    a=f/m;
    print(f"La masa es {m}");
else:
    print("Opción invalida");
print("\nGracias por utiliar este programa");