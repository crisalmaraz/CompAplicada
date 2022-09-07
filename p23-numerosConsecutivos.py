#Dados tres números enteros, verificar si son consecutivos (9,10,11) y mandar mensaje confirmándolo, si no lo son 
#(1,4,6) mandar mensaje de error

a,b,c=input().split();
a,b,c=int(a),int(b),int(c);

if ((a-b==1) and (b-c)==1):
    print("Son numeros consecutivos");
else:
    print("Error no son consecutivos");