# numeros de 1 a 200, suma 100
c = 0
suma = 0
while c<200 :
    c+=1
    suma+=c
    print(c,end=" ")
    if suma >= 100:
        break

print(f"\nHemos alcanzado el limite {suma}, sumando {c} números")