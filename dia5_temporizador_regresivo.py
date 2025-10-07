# bucles for y While
"""num = int(input("Introduce un numero: "))
for i in range(11):
    print(f"{num} x {i} = {num * i}")"""

"""import  time

for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("Feliz año nuevo!!!!!")"""

#Para el proyecto hay que tomar un número de cuenta regresiva y cuente hasta cero mostrando un número a la vez con un retraso de un segundo
import time
num = int(input("Ingresa un número: "))
tiempo = int(input("Ingresa el tiempo en segundos que quieres que espere la app: "))

for i in range(num,0,-1):
    print(i)
    time.sleep(tiempo)

print("Felicidades por llegar al final🏆🏆🏆🏆✨🏆✨🏆✨!!!!!!")



























