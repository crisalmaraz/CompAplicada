# operaciones entre conjuntos de numeros
import os; 
os.system('clear');

c1 = {1,2,3,4,5};
c2 = {5,6,7,8,9,10};
c3 = {9,10,11,12,13};
c4 = {3,4,5};

print(f"c1 : {c1}\nc2 : {c2}\nc3 : {c3}\nc4 :{c4}");
print("\nUnion: ");
print(f"c1 union c2 : {c1.union(c2)}");
print(f"c1 union c3 : {c1 | c3}");
print("\nIntersección: ");
print(f"c1 inteseccion c2: {c1.intersection(c2)}");
print(f"c2 interseccion c3: {c2 & c3}");
print("\nDiferencia:");
print(f"c1 diferencia c4: {c1.difference(c4)}");
print(f"c2 diferencia c3: {c2 - c3}");