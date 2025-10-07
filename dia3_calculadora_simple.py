# calculadora simple

# suma, resta multiplicación y división

num1 = float(input("Ingrse un número: "))
num2 = float(input("Ingrse otro número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "no se puede dividir por cero"
# usa cadenas f para imprimir los resultados
print("--- Calculadora simple ---")
print(f"La suma es: {num1} + {num2} = {suma}")
print(f"La resta es: {num1} - {num2} = {resta}")
print(f"La multiplicación es: {num1} * {num2} = {multiplicacion}")
print(f"La división es: {num1} / {num2} = {division}")






















