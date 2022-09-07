#Dados tres números enteros, verificar cual es el mayor.

a,b,c=input().split();
a,b,c=int(a),int(b),int(c);

if (a>b and a>c):
    print(f"El número mayor es {a}");
elif (b>a and b>c):
    print(f"El número mayor es {b}");
else:
    print(f"El número mayor es {c}");