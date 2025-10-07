#Comparacion de numeros con condicional if-else
# Proyecto: crear una herramienta de comparción de números

# se tiene que toamr dos números como entrada y compararlos. identifica cual es mayor o si son iguales y si alguno es cero

num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
print("\n")
print("--- Comparación de números ---")
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num1} es menor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual que {num2}")
print("-------------------------------------------")
if num1 == 0 or num2 == 0:
    print("Uno de los números es cero")
else:
    print("ambos números son diferentes de cero")
print("-------------------------------------------")
if num1 < 0:
    print(f"{num1} es negativo")
elif num1 > 0:
    print(f"{num1} es positivo")

if num2 < 0:
     print(f"{num2} es negativo")
elif num2 > 0:
     print(f"{num2} es positivo")
print("-------------------------------------------")

