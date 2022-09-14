# suma de n números y su promedio introducidos por el usuario:
print('Suma de n números y su promedio, introducidos por el usuario:')
n = int(input('Cuantos numeros: '));
suma = 0

for x in range(1,n+1,1):
    s = int(input(f"Número {x}: "));
    suma += s;

print(f'\nLa suma es {suma}');
print(f"El promedio es: {suma/n:.2f}")