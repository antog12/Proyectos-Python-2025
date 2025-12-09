import psutil

#Obtener la tupla con nombre (svmem)
memoria = psutil.virtual_memory()

#Imprimir la información clave
print(f"Total: {memoria.total / (1024**3):.2f} GB")
print(f"Disponible (Available): {memoria.available / (1024**3):.2f} GB")
print(f"Usada (Used): {memoria.used / (1024**3):.2f} GB")
print(f"Porcentaje de Uso: {memoria.percent}%")
