#funciones trigonometricas en python

import math

print("Uso de las funciones trigonometricas de python");

angulo=float(input("Dame un angulo en radiones: "));
seno= math.sin(angulo);
coseno= math.cos(angulo);
tangente= math.tan(angulo);

grado= math.degrees(angulo);

print(f"Seno {seno}, Coseno {coseno}, Tangente {tangente}, Grados: {grado}");

salida=(
    f"El seno es {seno:.2f} \n"
    f"El coseno es {coseno:.2f} \n"
    f"La tangente es {tangente:.2f} \n"
    f"El angulo es {angulo:.2f} en radianes, equivale a {grado:.2f} \n"
)
print(salida);
