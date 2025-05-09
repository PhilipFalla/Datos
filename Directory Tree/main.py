import os
import tree as t

def menu():
    print("\nBienvenido al generador de árbol de directorios.")
    print(f"\n**Directorio actual de trabajo: {os.getcwd()}**")

    while True:
        # Solicitar la ruta del directorio
        path = input("\nPor favor, ingrese la ruta del directorio que desea explorar (o escriba 'salir' para terminar): ")

        if path.lower() == 'salir':
            print("Saliendo del programa. ¡Hasta luego!")
            return

        if not os.path.exists(path):
            print("**El path especificado no existe. Asegúrese de escribirlo correctamente.**")
            continue  # Volver a pedir el path
        
        # Mostrar el path absoluto que se va a explorar
        print(f"\nExplorando el directorio: {os.path.abspath(path)}")
        
        # Generar el árbol
        tree = t.build_tree(path)
        
        # Mostrar el árbol de directorios
        print("\nÁrbol de directorios generado:")
        t.print_tree(tree)

        break  # Salimos del bucle de pedir path una vez que todo salió bien

    # Ahora seguimos al menú de opciones
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Ver el contenido de un archivo.")
        print("2. Salir.")
        
        choice = input("Elija una opción (1 o 2): ")
        
        if choice == '1':
            file_name = input("Ingrese el nombre del archivo (con su extensión) para ver su contenido: ")
            
            # Buscar el archivo en el árbol
            node = t.find_file_in_tree(tree, file_name)
            
            if node:
                t.print_file_content(node)
            else:
                print("El archivo no se encuentra en el directorio.")
        
        elif choice == '2':
            print("Gracias por usar el generador de árbol de directorios. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elija 1 o 2.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()