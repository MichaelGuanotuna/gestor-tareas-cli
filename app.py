tareas = []

def completar_tarea():
    numero = int(input("Numero de tarea: "))
    if numero >= 1 and numero <= len(tareas):
        tareas[numero - 1] = "[X] " + tareas[numero - 1]
        print("Tarea completada")

def eliminar_tarea():
    numero = int(input("Numero de tarea: "))
    if numero >= 1 and numero <= len(tareas):
        tareas.pop(numero - 1)
        print("Tarea eliminada")

def mostrar_menu():
    while True:
        print("=== GESTOR DE TAREAS ===")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "0":
            break

if __name__ == "__main__":
    mostrar_menu()
