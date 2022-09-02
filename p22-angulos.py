#Dado un ángulo entre 0 y 360 mostrar el tipo de angulo
# <90 agudo, =90 recto y <180 obtuso, =180 llano y <360 concavo

print("Mostrar el tipo de angulo en base a los grados");
angulo= int(input("Dame un angulo (0..360): "));

if angulo>=0 and angulo<=360:
    if (angulo<90):
        print("Agudo");
    elif (angulo==90):
        print("Recto");
    elif (angulo>90 and angulo<180):
        print("Obtuso");
    elif (angulo==180):
        print("LLano");
    elif (angulo>180 and angulo<360):
        print("Concavo");
else:
    print(f"El angulo {angulo} esta fuera de rango");
