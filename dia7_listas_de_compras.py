# proyecto basado en listas

#lista_de_compra = ["leche","pan","huevos","azúcar"]

"""print(lista_de_compra)

# operaciones con listas

print(lista_de_compra[1])

lista_de_compra.append("tortitas")

print(lista_de_compra)

lista_de_compra.insert(1,"zumo")

print(lista_de_compra)

lista_de_compra.remove("zumo")

print(lista_de_compra)

lista_de_compra.pop()

print(lista_de_compra)"""

"""for i in lista_de_compra:
    print(f"- {i}")"""

"""for index, item in enumerate(lista_de_compra):
    print(f"{index+1}. {item}")"""

# aplicación de listas de compras:
"""- agregar artículos a la lista.
- eliminar artículos de la lista.
- vamos a ver todos los artículos de la lista.
- escribiremos un código para salir del programa."""

lista_de_compras = []

def show_menu():
    print("\n--- Menú de la lista de compras ---")
    print("1. Ver todos los artículos de la lista")
    print("2. Agregar artículo a la lista")
    print("3. Eliminar artículo de la lista")
    print("4. Limpiar la lista")
    print("5. Salir del programa")


while True:
    show_menu()
    choice = int(input("Selecciona una opción (1-5): "))

    if choice == 1:
        print("\n--- Lista de compras ---")
        if not lista_de_compras:
            print("Tu lista de compras está vacía")
        else:
            for index,item in enumerate(lista_de_compras):
                print(f"{index+1}. {item}")

    elif choice == 2:
        item = input("Ingresa el artículo a agregar: ")
        lista_de_compras.append(item)
        print(f"{item} ha sido agregado a la lista")

    elif choice == 3:
        item = input("Ingresa el artículo a eliminar: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"{item} ha sido eliminado de la lista")
        else:
            print(f"{item} no se encuentra en la lista")

    elif choice == 4:
        lista_de_compras.clear()
        print("La lista de compras ha sido limpiada")

    elif choice == 5:
        print("¡Hasta luego!")
        break

    else:
        print("Elección inválida. Por favor, selecciona una opción válida.")











