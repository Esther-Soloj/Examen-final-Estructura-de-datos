class Nodo:
    def __init__(self, id, datos):
        self.id = id
        self.datos = datos
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def agregar_estudiante(self, id, datos):
        if self.raiz is None:
            self.raiz = Nodo(id, datos)
        else:
            self._agregar(self.raiz, id, datos)

    def _agregar(self, nodo, id, datos):
        if id < nodo.id:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(id, datos)
            else:
                self._agregar(nodo.izquierdo, id, datos)
        elif id > nodo.id:
            if nodo.derecho is None:
                nodo.derecho = Nodo(id, datos)
            else:
                self._agregar(nodo.derecho, id, datos)

    def buscar_estudiante(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if nodo is None or nodo.id == id:
            return nodo
        if id < nodo.id:
            return self._buscar(nodo.izquierdo, id)
        else:
            return self._buscar(nodo.derecho, id)

    def eliminar_estudiante(self, id):
        self.raiz = self._eliminar(self.raiz, id)

    def _eliminar(self, nodo, id):
        if nodo is None:
            return nodo
        if id < nodo.id:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, id)
        elif id > nodo.id:
            nodo.derecho = self._eliminar(nodo.derecho, id)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo
            temp = self._min_value_node(nodo.derecho)
            nodo.id = temp.id
            nodo.datos = temp.datos
            nodo.derecho = self._eliminar(nodo.derecho, temp.id)
        return nodo

    def _min_value_node(self, nodo):
        current = nodo
        while current.izquierdo is not None:
            current = current.izquierdo
        return current

    def listar_estudiantes(self):
        estudiantes = []
        self._inorden(self.raiz, estudiantes)
        return estudiantes

    def _inorden(self, nodo, estudiantes):
        if nodo:
            self._inorden(nodo.izquierdo, estudiantes)
            estudiantes.append((nodo.id, nodo.datos))
            self._inorden(nodo.derecho, estudiantes)

    def dibujar_arbol(self):
        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            self._imprimir_arbol(self.raiz, "", True)

    def _imprimir_arbol(self, nodo, indent, last):
        if nodo is not None:
            print(indent, end="")
            if last:
                print("└─", end="")
                indent += "   "
            else:
                print("├─", end="")
                indent += "|  "

            print(f"{nodo.id} ({nodo.datos['nombre']}, {nodo.datos['telefono']})")

            self._imprimir_arbol(nodo.izquierdo, indent, False)
            self._imprimir_arbol(nodo.derecho, indent, True)

def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\nMenu:")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Eliminar Estudiante")
        print("4. Listar Estudiantes")
        print("5. Listar estudiantes en un archivo")
        print("6. Dibujar Árbol en Consola")
        print("7. Intrucciones de uso del programa")
        print("8. salir ")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("Ingrese el ID del estudiante: "))
            nombre = input("Ingrese el nombre del estudiante: ")
            telefono = input("Ingrese el número de teléfono del estudiante: ")
            datos = {'nombre': nombre, 'telefono': telefono}
            arbol.agregar_estudiante(id, datos)
            print(f"Estudiante con ID {id} agregado.")

        elif opcion == '2':
            id = int(input("Ingrese el ID del estudiante a buscar: "))
            estudiante = arbol.buscar_estudiante(id)
            if estudiante:
                print(f"Estudiante encontrado: ID {estudiante.id}, Nombre {estudiante.datos['nombre']}, Teléfono {estudiante.datos['telefono']}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == '3':
            id = int(input("Ingrese el ID del estudiante a eliminar: "))
            arbol.eliminar_estudiante(id)
            print(f"Estudiante con ID {id} eliminado.")

        elif opcion == '4':
            estudiantes = arbol.listar_estudiantes()
            print("Lista de estudiantes en orden ascendente:")
            for id, datos in estudiantes:
                print(f"ID {id}, Nombre {datos['nombre']}, Teléfono {datos['telefono']}")

        elif opcion == '5':
            estudiantes = arbol.listar_estudiantes()
            with open('estudiantes.txt', 'w') as archivo:
                for id, datos in estudiantes:
                    archivo.write(f"ID {id}, Nombre {datos['nombre']}, Teléfono {datos['telefono']}\n")
            print("Lista de estudiantes guardada en 'estudiantes.txt'.")

        elif opcion == '6':
            arbol.dibujar_arbol()

        elif opcion == "7":
            print("En el menu se seleciona cada accion , al agregar estudiantes pide el id, nombre y telefono")
            print("al exportar el archivo se guarda en orden ascendete con el id y la informacion del estudiante")
            print("el programa es bastante intuitivo")

        elif opcion == '8':
            print("Peograma hecho por Esther Soloj, gracias por utilizarlo")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
