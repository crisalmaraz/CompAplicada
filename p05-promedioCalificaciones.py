#Calcular la suma y el promedio de 3 calificaciones
print("Calcular la suma y el promedio de 3 calificaciones \n");

#c1=int(intput("Dame calificación 1: "));
#c2=int(intput("Dame calificación 2: "));
#c3=int(intput("Dame calificación 3: "));

print("Dame tres caificaciones separadas por un espacio");
c1,c2,c3 = input().split();
c1,c2,c3 =[int(c1),int(c2),int(c3)];
suma= c1+c2+c3;
prom=suma/3;
print(f"Los numeros fueron {c1}, {c2}, {c3}");
print(f"La suma {suma}");
print(f"El promedio {prom}")
