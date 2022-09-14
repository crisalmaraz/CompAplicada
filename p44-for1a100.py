#ciclo for del 1 al 100

#print("\n números del 1 al 100 de uno en uno");

#for n in range(1,101,1):
#    print(n, end=" ");

# print("\n números del 1 a n de uno en uno");

# n=int(input("Hasta donde sera: "));
# for x in range(1,n+1,1):
#     print(x, end=" ");

print("\n números del 1 a n con incremento de uno en uno");

n=int(input("Hasta donde sera: "));
i=int(input("Incremento: "));
for x in range(1,n+1,i):
    print(x, end=" ");



