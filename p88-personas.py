#Operaciones con conjuntos

A={"Juan","Maria","Pedro","Jose","Rocio"};
B={"Pedro","Juan","Pablo","Mateo","Esther"};

print(f"Conjunto A: {A}");
print(f"Conjunto B: {B}");

print(f"Union A Y B: {A|B}");
print(f"Intersección A Y B: {A&B}");
print(f"Diferencia A Y B: {A-B}");
print(f"Diferencia simetrica A Y B: {A^B}");

if {"Pablo","Mateo"}.issubset(B):
    print(f"Pablo y Mateo son subconjunto de B {B}");
else:
    print(f"Pablo y Mateo no son subconjunto de B {B}");

if A.issuperset({"Reynaldo","Angelica"}):
    print(f"A es superconjunto de Reynaldo y Angelica");
else:
    print(f"A no es superconjunto de Reynaldo y Angelica");

if "Pedro" in A:
    print("Pedro esta en A");
else:
    print("Pedro no esta en A");

if not "Lila" in B:
    print("Lila no esta en B");
else:
    print("Lila esta en A");