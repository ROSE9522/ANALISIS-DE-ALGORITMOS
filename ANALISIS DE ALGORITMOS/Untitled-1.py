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
