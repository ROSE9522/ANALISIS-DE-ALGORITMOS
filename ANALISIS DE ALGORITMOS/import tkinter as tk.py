import tkinter as tk
from tkinter import messagebox

class NodoPaciente:
    def _init_(self, nombre, gravedad):
        self.nombre = nombre
        self.gravedad = gravedad
        self.siguiente = None

class ListaEmergencia:
    def _init_(self):
        self.primer_paciente = None
        self.registro = []

    def agregar_paciente(self, nombre, gravedad):
        nuevo_paciente = NodoPaciente(nombre, gravedad)
        self.registro.append(nuevo_paciente)
        if not self.primer_paciente:
            self.primer_paciente = nuevo_paciente
        else:
            actual = self.primer_paciente
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_paciente

    def atender_emergencia(self):
        if not self.primer_paciente:
            messagebox.showinfo("Info", "No hay pacientes en espera.")
            return
        paciente = self._encontrar_mas_grave(None, self.primer_paciente, None)
        messagebox.showinfo("Atención de emergencia", f"Atendiendo a {paciente.nombre} con gravedad {paciente.gravedad}")
        self.eliminar_paciente(paciente)

    def _encontrar_mas_grave(self, prev, actual, mas_grave):
        if not actual:
            return mas_grave
        if not mas_grave or actual.gravedad > mas_grave.gravedad:
            mas_grave = actual
        return self._encontrar_mas_grave(actual, actual.siguiente, mas_grave)

    def eliminar_paciente(self, paciente):
        if self.primer_paciente == paciente:
            self.primer_paciente = self.primer_paciente.siguiente
        else:
            actual = self.primer_paciente
            while actual.siguiente != paciente:
                actual = actual.siguiente
            actual.siguiente = paciente.siguiente
        self.registro.remove(paciente)

    def mostrar_lista(self):
        if not self.primer_paciente:
            messagebox.showinfo("Info", "No hay pacientes en espera.")
            return
        lista_pacientes = "Lista de pacientes en espera:\n"
        actual = self.primer_paciente
        while actual:
            lista_pacientes += f"{actual.nombre} - Gravedad: {actual.gravedad}\n"
            actual = actual.siguiente
        lista_pacientes
        lista_pacientes += "\nRegistro de todos los pacientes ingresados:\n"
        for paciente in self.registro:
            lista_pacientes += f"{paciente.nombre} - Gravedad: {paciente.gravedad}\n"
        messagebox.showinfo("Lista de pacientes en espera", lista_pacientes)

class AplicacionHospital:
    def _init_(self, ventana):
        self.ventana = ventana
        self.ventana.title("Hospital - Lista de Emergencia")

        self.lista_emergencia = ListaEmergencia()

        self.etiqueta_titulo = tk.Label(ventana, text="Sistema de Lista de Emergencia del Hospital", font=("Arial", 14))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.boton_agregar = tk.Button(ventana, text="Agregar Paciente", command=self.agregar_paciente)
        self.boton_agregar.grid(row=1, column=0, padx=10, pady=5)

        self.boton_atender = tk.Button(ventana, text="Atender Emergencia", command=self.atender_emergencia)
        self.boton_atender.grid(row=1, column=1, padx=10, pady=5)

        self.frame_lista = tk.Frame(ventana)
        self.frame_lista.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.lista_pacientes = tk.Listbox(self.frame_lista)
        self.lista_pacientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_lista = tk.Scrollbar(self.frame_lista, orient=tk.VERTICAL)
        self.scrollbar_lista.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_pacientes.config(yscrollcommand=self.scrollbar_lista.set)
        self.scrollbar_lista.config(command=self.lista_pacientes.yview)

        self.boton_eliminar = tk.Button(ventana, text="Eliminar Paciente", command=self.eliminar_paciente)
        self.boton_eliminar.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.mostrar_lista()

    def agregar_paciente(self):
        ventana_agregar = tk.Toplevel()
        ventana_agregar.title("Agregar Paciente")

        tk.Label(ventana_agregar, text="Nombre del paciente:").grid(row=0, column=0)
        tk.Label(ventana_agregar, text="Gravedad (1-10):").grid(row=1, column=0)

        nombre_entry = tk.Entry(ventana_agregar)
        nombre_entry.grid(row=0, column=1)
        gravedad_entry = tk.Entry(ventana_agregar)
        gravedad_entry.grid(row=1, column=1)

        boton_agregar = tk.Button(ventana_agregar, text="Agregar", command=lambda: self._agregar_desde_ventana(nombre_entry.get(), gravedad_entry.get(), ventana_agregar))
        boton_agregar.grid(row=2, column=0, columnspan=2, pady=5)

    def _agregar_desde_ventana(self, nombre, gravedad, ventana):
        try:
            gravedad = int(gravedad)
            if gravedad < 1 or gravedad > 10:
                messagebox.showerror("Error", "La gravedad debe estar entre 1 y 10.")
            else:
                self.lista_emergencia.agregar_paciente(nombre, gravedad)
                messagebox.showinfo("Info", "Paciente agregado a la lista de emergencia.")
                ventana.destroy()
                self.mostrar_lista()
        except ValueError:
            messagebox.showerror("Error", "La gravedad debe ser un número entero.")

    def atender_emergencia(self):
        self.lista_emergencia.atender_emergencia()
        self.mostrar_lista()

    def mostrar_lista(self):
        self.lista_pacientes.delete(0, tk.END)
        for paciente in self.lista_emergencia.registro:
            self.lista_pacientes.insert(tk.END, f"{paciente.nombre} - Gravedad: {paciente.gravedad}")

    def eliminar_paciente(self):
        seleccionado = self.lista_pacientes.curselection()
        if not seleccionado:
            messagebox.showerror("Error", "Seleccione un paciente para eliminar.")
            return
        indice = seleccionado[0]
        paciente = self.lista_emergencia.registro[indice]
        self.lista_emergencia.eliminar_paciente(paciente)
        self.mostrar_lista()

def main():
    ventana_principal = tk.Tk()
    aplicacion = AplicacionHospital(ventana_principal)
    ventana_principal.mainloop()

if _name_ == "_main_":
    main()