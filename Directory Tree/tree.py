import os

class Node():
    def __init__(self, name: str, content: str = ""):
        self.name = name
        self.content = content

class Tree():
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def insert_child(self, obj: any):
        self.children.append(obj)

    def get_children(self):
        return self.children

def build_tree(path):
    # Construye el árbol a partir de un path
    tree = Tree(os.path.basename(path) or path)

    try:
        entries = os.listdir(path)
    except PermissionError:
        entries = []
    
    for entry in entries:
        # Si es una carpeta oculta, la ignoramos
        if entry.startswith('.'):
            continue
        
        full_path = os.path.join(path, entry)

        # Si es folder, agregar hijo de folder y repetir
        if os.path.isdir(full_path):
            subtree = build_tree(full_path)
            tree.insert_child(subtree)

        # Si es archivo, es una hoja y creamos el nodo
        else:
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()  # Leemos todo el contenido del archivo
            except Exception:
                content = "[No se pudo leer el archivo]"
            node = Node(entry, content)
            tree.insert_child(node)
    
    return tree

def print_tree(tree, indent=""):
    # Imprime el árbol solo con nombres de carpetas y archivos
    print(indent + f"- {tree.name}/")
    indent += "    "
    for child in tree.get_children():
        if isinstance(child, Tree):
            print_tree(child, indent)
        else:
            print(indent + f"- {child.name}")

def print_file_content(node):
    """Imprime el contenido de un archivo Node"""
    print(f"\nContenido de {node.name}:\n")
    print(node.content)

def find_file_in_tree(tree, file_name):
    """Busca un archivo en el árbol de directorios"""
    for child in tree.get_children():
        if isinstance(child, Tree):
            # Recursión para buscar en subdirectorios
            node = find_file_in_tree(child, file_name)
            if node:
                return node
        elif child.name == file_name:
            return child
    return None