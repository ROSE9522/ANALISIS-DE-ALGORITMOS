import tkinter as tk
from tkinter import messagebox

# Definición de la clase Producto para manejar los datos del producto
class Producto:
    def __init__(self, identificador, nombre, precio, cantidad):
        # Inicializa los atributos del producto
        self.id = identificador
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __repr__(self):
        # Representación del objeto cuando se imprime
        return f"{self.nombre} (ID: {self.id}, Precio: {self.precio}, Cantidad: {self.cantidad})"

# Implementa el algoritmo Merge Sort para ordenar productos por precio
def merge_sort_precio(productos):
    if len(productos) > 1:
        # Encuentra el punto medio de la lista
        mid = len(productos) // 2
        # Divide la lista en dos mitades
        L = productos[:mid]
        R = productos[mid:]

        # Llamadas recursivas para dividir la lista en mitades
        merge_sort_precio(L)
        merge_sort_precio(R)

        i = j = k = 0
        
        # Fusionar las dos mitades ordenadas
        while i < len(L) and j < len(R):
            if L[i].precio < R[j].precio:
                productos[k] = L[i]
                i += 1
            else:
                productos[k] = R[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de L, si hay
        while i < len(L):
            productos[k] = L[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de R, si hay
        while j < len(R):
            productos[k] = R[j]
            j += 1
            k += 1

# Implementa el algoritmo Quick Sort para ordenar productos por nombre
def quick_sort_nombre(productos, low, high):
    if low < high:
        # Encuentra el índice de partición
        pi = partition_nombre(productos, low, high)
        
        # Ordena los elementos antes y después de la partición
        quick_sort_nombre(productos, low, pi - 1)
        quick_sort_nombre(productos, pi + 1, high)

# Función de partición para Quick Sort
def partition_nombre(productos, low, high):
    # El pivote es el último elemento
    pivot = productos[high].nombre
    i = low - 1
    for j in range(low, high):
        if productos[j].nombre < pivot:
            i += 1
            # Intercambia productos[i] con productos[j]
            productos[i], productos[j] = productos[j], productos[i]
    # Intercambia el pivote con el elemento en i+1
    productos[i + 1], productos[high] = productos[high], productos[i + 1]
    return i + 1

# Implementa el algoritmo Cocktail Shaker Sort para ordenar productos por cantidad
def cocktail_sort_cantidad(productos):
    n = len(productos)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        
        # Recorrido hacia adelante
        for i in range(start, end):
            if productos[i].cantidad > productos[i + 1].cantidad:
                productos[i], productos[i + 1] = productos[i + 1], productos[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        
        # Recorrido hacia atrás
        for i in range(end - 1, start - 1, -1):
            if productos[i].cantidad > productos[i + 1].cantidad:
                productos[i], productos[i + 1] = productos[i + 1], productos[i]
                swapped = True
        start += 1

# Funciones para manejar el inventario
def agregar_producto(inventario, producto):
    # Agrega un producto al inventario
    inventario.append(producto)

def buscar_producto(inventario, identificador):
    # Busca un producto en el inventario por su ID
    for producto in inventario:
        if producto.id == identificador:
            return producto
    return None

def eliminar_producto(inventario, identificador):
    # Elimina un producto del inventario por su ID
    producto = buscar_producto(inventario, identificador)
    if producto:
        inventario.remove(producto)

# Definición de la clase App para la interfaz gráfica
class App:
    def __init__(self, root):
        self.root = root
        # Establece el título de la ventana principal
        self.root.title("Inventario de Productos")
        self.inventario = []
        self.insertar_datos_ejemplo()
        self.create_widgets()

    def create_widgets(self):
        """Crea los componentes de la interfaz gráfica."""
        # Etiquetas y entradas para ID, nombre, precio y cantidad
        tk.Label(self.root, text="ID:").grid(row=0, column=0)
        tk.Label(self.root, text="Nombre:").grid(row=1, column=0)
        tk.Label(self.root, text="Precio:").grid(row=2, column=0)
        tk.Label(self.root, text="Cantidad:").grid(row=3, column=0)
        self.entry_id = tk.Entry(self.root)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_precio = tk.Entry(self.root)
        self.entry_cantidad = tk.Entry(self.root)
        self.entry_id.grid(row=0, column=1)
        self.entry_nombre.grid(row=1, column=1)
        self.entry_precio.grid(row=2, column=1)
        self.entry_cantidad.grid(row=3, column=1)

        # Botones para agregar, buscar, eliminar y ordenar productos
        tk.Button(self.root, text="Agregar", command=self.agregar_producto).grid(row=4, column=0)
        tk.Button(self.root, text="Buscar", command=self.buscar_producto).grid(row=4, column=1)
        tk.Button(self.root, text="Eliminar", command=self.eliminar_producto).grid(row=4, column=2)
        tk.Button(self.root, text="Ordenar por Precio", command=self.ordenar_por_precio).grid(row=5, column=0)
        tk.Button(self.root, text="Ordenar por Nombre", command=self.ordenar_por_nombre).grid(row=5, column=1)
        tk.Button(self.root, text="Ordenar por Cantidad", command=self.ordenar_por_cantidad).grid(row=5, column=2)

        # Listbox para mostrar el inventario
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=6, column=0, columnspan=3)
        self.actualizar_listbox()

    def insertar_datos_ejemplo(self):
        # Inserta algunos datos de ejemplo en el inventario
        productos_ejemplo = [
            Producto("001", "Manzana", 0.50, 100),
            Producto("002", "Banana", 0.30, 150),
            Producto("003", "Naranja", 0.80, 200),
            Producto("004", "Fresa", 1.50, 50),
            Producto("005", "Uva", 2.00, 75)]
        self.inventario.extend(productos_ejemplo)

    def agregar_producto(self):
        # Agrega un producto desde la interfaz gráfica
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        precio = float(self.entry_precio.get())
        cantidad = int(self.entry_cantidad.get())
        producto = Producto(id, nombre, precio, cantidad)
        agregar_producto(self.inventario, producto)
        self.actualizar_listbox()

    def buscar_producto(self):
        # Busca un producto en la interfaz gráfica
        id = self.entry_id.get()
        producto = buscar_producto(self.inventario, id)
        if producto:
            messagebox.showinfo("Producto Encontrado", str(producto))
        else:
            messagebox.showwarning("No Encontrado", "Producto no encontrado")

    def eliminar_producto(self):
        # Elimina un producto desde la interfaz gráfica
        id = self.entry_id.get()
        eliminar_producto(self.inventario, id)
        self.actualizar_listbox()

    def ordenar_por_precio(self):
        # Ordena el inventario por precio
        merge_sort_precio(self.inventario)
        self.actualizar_listbox()

    def ordenar_por_nombre(self):
        # Ordena el inventario por nombre
        quick_sort_nombre(self.inventario, 0, len(self.inventario) - 1)
        self.actualizar_listbox()

    def ordenar_por_cantidad(self):
        # Ordena el inventario por cantidad
        cocktail_sort_cantidad(self.inventario)
        self.actualizar_listbox()

    def actualizar_listbox(self):
        # Actualiza el Listbox con los productos en el inventario
        self.listbox.delete(0, tk.END)
        for producto in self.inventario:
            self.listbox.insert(tk.END, producto)

# Punto de entrada principal del programa
if __name__ == "__main__":
    # Crea la ventana principal de Tkinter
    root = tk.Tk()
    # Crea la aplicación con la ventana principal
    app =  (root)
    # In
