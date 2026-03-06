import tkinter as tk
from funciones_excel import agregar_a_excel # Asumiendo que esta función existe

def abrir_modo_manual():
    ventana_manual = tk.Toplevel()
    ventana_manual.title("Modo Manual - Inventario LEGO")
    # No es necesario especificar la geometría si usas pack y grid correctamente,
    # ya que Tkinter ajustará el tamaño al contenido. Pero lo mantendremos:
    ventana_manual.geometry("580x450") 

    # 1. Botón Volver - Usamos PACK (en la ventana Toplevel)
    def volver():
        ventana_manual.destroy()
    tk.Button(ventana_manual, text="⬅ Volver", command=volver, bg="#f0f0f0").pack(padx=10, pady=10, anchor="nw")

    # 2. **SOLUCIÓN:** Crear un Frame para el contenido principal (donde se usará GRID)
    # Este Frame se ubicará con PACK en el Toplevel, evitando el conflicto.
    frame_contenido = tk.Frame(ventana_manual)
    frame_contenido.pack(padx=20, pady=10, fill="both", expand=True) # Usamos PACK aquí

    labels = ["ID Pieza", "Descripción", "Color", "Cantidad", "Set Origen", "Ubicación"]
    entries = []

    # 3. Campos de Entrada y Etiquetas - Usamos GRID (dentro del frame_contenido)
    for i, label in enumerate(labels):
        # Usar el frame_contenido como padre
        tk.Label(frame_contenido, text=label + ":").grid(row=i, column=0, sticky="w", padx=5, pady=5)
        entry = tk.Entry(frame_contenido, width=40) # Establecer un ancho para mejor presentación
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    # 4. Botón Agregar Pieza - Usamos GRID (dentro del frame_contenido)
    def agregar_manual():
        # Lógica para agregar a Excel
        print(f"Agregando: {entries[0].get()}, {entries[1].get()}, {entries[2].get()}, {entries[3].get()}, {entries[4].get()}, {entries[5].get()}")
        agregar_a_excel(entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get(), entries[5].get())
        
        # Limpiar campos
        for e in entries:
            e.delete(0, tk.END)

    tk.Button(frame_contenido, text="Agregar Pieza", command=agregar_manual, bg="lightgreen").grid(row=len(labels), column=0, columnspan=2, pady=15)
    
    # Opcional: Centrar los widgets en el frame_contenido si el frame se expande
    frame_contenido.grid_columnconfigure(0, weight=1)
    frame_contenido.grid_columnconfigure(1, weight=1)


# Ejemplo de cómo se llamaría:
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.withdraw() # Oculta la ventana principal, si solo quieres mostrar Toplevel
#     abrir_modo_manual()
#     root.mainloop()