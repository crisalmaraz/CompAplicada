#ciclo for del 100 a 1

# print("\n números del 100 al 1 de uno en uno");

# for n in range(100,0,-1):
#    print(n, end=" ");

# print("\n números del 100 a n de uno en uno");

# n=int(input("Hasta donde sera: "));
# for x in range(100,n-1,-1):
#     print(x, end=" ");

print("\n números del 100 a n con incremento de uno en uno");

n=int(input("Hasta donde sera: "));
i=int(input("Incremento: "));
for x in range(100,n-1,i):
    print(x, end=" ");