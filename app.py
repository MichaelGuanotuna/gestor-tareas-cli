tareas = []

def agregar_tarea():
    titulo = input("Nombre de la tarea: ")
    if titulo.strip() == "":
        print("Error: el titulo no puede estar vacio")
        return
    tareas.append(titulo)
    print("Tarea agregada")

def listar_tareas():
    for i in range(len(tareas)):
        print(i + 1, tareas[i])

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
        print("=== GESTOR DE TAREAS - MENU PRINCIPAL ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "0":
            break

if __name__ == "__main__":
    mostrar_menu()
