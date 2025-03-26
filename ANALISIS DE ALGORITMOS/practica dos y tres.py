
class Nodo:
    def __init__(self, dato):
        self.Puntero = None
        self.dato = dato

class L_enlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_aux = self.cabeza
            while nodo_aux.Puntero:
                nodo_aux = nodo_aux.Puntero
            nodo_aux.Puntero = nuevo_nodo
    def eliminar_elemento(self, dato):
        nodo_aux = self.cabeza
        if nodo_aux and nodo_aux.dato == dato:
            self.cabeza = nodo_aux.Puntero
            nodo_aux = None
            return
        nodo_aux2 = None
        while nodo_aux and nodo_aux.dato != dato:
            nodo_aux2 = nodo_aux
            nodo_aux = nodo_aux.Puntero

        if not nodo_aux:
            return
        
        nodo_aux2.Puntero = nodo_aux.Puntero
        nodo_aux = None

    def imprimir_lista(self):
        nodo_aux = self.cabeza
        while nodo_aux:
            print(nodo_aux.dato, end=" -> ")
            nodo_aux = nodo_aux.Puntero
        print("None")

lista = L_enlazada()
lista.agregar_elemento(5)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.imprimir_lista()
lista.eliminar_elemento(3)
lista.imprimir_lista()

def eliminar_elemento(self, dato):
    # Inicializamos un nodo auxiliar con la cabeza de la lista
    nodo_aux = self.cabeza

    # Comprobamos si la lista no está vacía y si el dato a eliminar está en la cabeza
    if nodo_aux and nodo_aux.dato == dato:
        # Si es así, actualizamos la cabeza de la lista para que apunte al siguiente nodo
        self.cabeza = nodo_aux.Puntero
        # Liberamos la memoria del nodo que estamos eliminando
        nodo_aux = None
        # Salimos del método ya que hemos eliminado el nodo deseado
        return

    # Inicializamos un nodo auxiliar para rastrear el nodo anterior al que estamos buscando
    nodo_aux2 = None

    # Recorremos la lista enlazada buscando el nodo con el dato a eliminar
    while nodo_aux and nodo_aux.dato != dato:
        # Actualizamos el nodo auxiliar que rastrea el nodo anterior
        nodo_aux2 = nodo_aux
        # Avanzamos al siguiente nodo en la lista
        nodo_aux = nodo_aux.Puntero

    # Si no encontramos el nodo con el dato a eliminar, salimos del método
    if not nodo_aux:
        return
    
    # Actualizamos el puntero del nodo anterior para que salte el nodo que estamos eliminando
    nodo_aux2.Puntero = nodo_aux.Puntero
    # Liberamos la memoria del nodo que estamos eliminando
    nodo_aux = None
