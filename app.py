tareas = []

def agregar_tarea():
    titulo = input("Nombre de la tarea: ")
    tareas.append(titulo)
    print("Tarea agregada")

def listar_tareas():
    for i in range(len(tareas)):
        print(i + 1, tareas[i])

def mostrar_menu():
    while True:
        print("=== GESTOR DE TAREAS - MENU PRINCIPAL ===")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("0. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "0":
            break

if __name__ == "__main__":
    mostrar_menu()
