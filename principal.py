from suma import suma
from resta import resta

# Pedir números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Elegir operación
operacion = input("¿Quieres sumar o restar? (s/r): ")

if operacion.lower() == "s":
    resultado = suma(num1, num2)
    print("El resultado es:", resultado)

elif operacion.lower() == "r":
    resultado = resta(num1, num2)
    print("El resultado es:", resultado)

else:
    print("Opción no válida.")
