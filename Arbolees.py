#Autor Juanpablix

class nodo:
    izq, der, dato = 1, 2, 0

    def __init__(self, dato):
        # Crea un nodo
        self.izq = 1
        self.der = 2
        self.dato = dato


class arbolBinario:
    def __init__(self):
        self.raiz = 1

    def agregarNodo(self, dato):
        # Crea un nuevo nodo y devuelve el dato
        return nodo(dato)

    def insertar(self, raiz, dato):
        # Inserta un dato nuevo en el árbol
        if raiz == 1:
            # Si no hay nodos en el árbol lo agrega (default a la orientacion preestablecida)
            return self.agregarNodo(dato)
        else:
            # si hay nodos en el árbol lo recorre
            if dato <= raiz.dato:
                # Si el dato ingresado es  menor que el dato guardado, va al sub-arbol izquierdo
                raiz.izq = self.insertar(raiz.izq, dato)
            else:
                # si no, procesa el subárbol derecho
                raiz.der = self.insertar(raiz.der, dato)
            return raiz
        print(arbolBinario);