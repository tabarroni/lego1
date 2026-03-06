<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import openpyxl
import os

EXCEL_FILE = "inventario_lego.xlsx"

# ===========================================
# Crear el Excel si no existe
# ===========================================
if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    hoja = wb.active
    hoja.title = "Piezas"
    hoja.append(["ID Pieza", "Descripción", "Color", "Cantidad", "Set Origen", "Ubicación"])
    wb.save(EXCEL_FILE)


# ===========================================
# Ventana de edición del archivo
# ===========================================
def editar_archivo():
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Archivo - Inventario LEGO")
    ventana_editar.geometry("800x500")

    archivo_abierto = None
    df_actual = None
    tree = None

    # ----------------------------
    # Buscar archivo manualmente
    # ----------------------------
    def buscar_archivo():
        nonlocal archivo_abierto
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx *.xls")]
        )
        if ruta:
            archivo_abierto = ruta
            abrir_archivo()

    # ----------------------------
    # Abrir y mostrar archivo
    # ----------------------------
    def abrir_archivo():
        nonlocal df_actual, tree, archivo_abierto

        if not archivo_abierto:
            archivo_abierto = EXCEL_FILE

        try:
            df_actual = pd.read_excel(archivo_abierto)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")
            return

        # Limpiar tabla anterior
        for widget in frame_tabla.winfo_children():
            widget.destroy()

        # Crear tabla
        tree = ttk.Treeview(frame_tabla, columns=list(df_actual.columns), show="headings", height=15)
        for col in df_actual.columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        for _, fila in df_actual.iterrows():
            tree.insert("", "end", values=list(fila))

        tree.pack(fill="both", expand=True)

        # Permitir doble clic en "Cantidad"
        tree.bind("<Double-1>", editar_celda)

    # ----------------------------
    # Editar celda (solo "Cantidad")
    # ----------------------------
    def editar_celda(event):
        nonlocal df_actual, tree

        item_id = tree.identify_row(event.y)
        col_id = tree.identify_column(event.x)
        if not item_id or not col_id:
            return

        col_index = int(col_id.replace("#", "")) - 1
        col_name = df_actual.columns[col_index]
        if col_name != "Cantidad":
            messagebox.showinfo("Edición no permitida", "Solo se puede modificar la columna 'Cantidad'.")
            return

        valores = tree.item(item_id, "values")
        valor_actual = valores[col_index]

        top = tk.Toplevel(ventana_editar)
        top.title("Editar cantidad")
        tk.Label(top, text=f"Cantidad actual: {valor_actual}").pack(pady=5)
        entrada = tk.Entry(top)
        entrada.insert(0, valor_actual)
        entrada.pack(pady=5)

        def confirmar():
            nuevo_valor = entrada.get()
            try:
                nuevo_valor = int(nuevo_valor)
            except ValueError:
                messagebox.showerror("Error", "Debe ser un número entero.")
                return

            # Actualizar DataFrame
            id_pieza = valores[0]
            idx = df_actual.index[df_actual["ID Pieza"] == id_pieza]
            if len(idx) == 0:
                messagebox.showerror("Error", "No se encontró el ID en el archivo.")
                top.destroy()
                return

            df_actual.loc[idx, "Cantidad"] = nuevo_valor
            df_actual.to_excel(archivo_abierto, index=False)

            # Actualizar tabla
            tree.item(item_id, values=tuple(
                nuevo_valor if i == col_index else v for i, v in enumerate(valores)
            ))

            top.destroy()
            messagebox.showinfo("Éxito", "Cantidad actualizada correctamente.")

        tk.Button(top, text="Guardar", command=confirmar).pack(pady=5)

    # ----------------------------
    # Cerrar archivo
    # ----------------------------
    def cerrar_archivo():
        nonlocal archivo_abierto, df_actual
        archivo_abierto = None
        df_actual = None
        for widget in frame_tabla.winfo_children():
            widget.destroy()
        messagebox.showinfo("Cerrar archivo", "Archivo cerrado correctamente.")

    # ----------------------------
    # Volver
    # ----------------------------
    def volver():
        ventana_editar.destroy()

    # ----------------------------
    # Interfaz gráfica
    # ----------------------------
    tk.Button(ventana_editar, text="⬅ Volver", command=volver, bg="#f0f0f0").pack(padx=10, pady=10, anchor="nw")

    frame_botones = tk.Frame(ventana_editar)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Buscar Archivo", command=buscar_archivo, bg="lightblue").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Abrir Archivo", command=abrir_archivo, bg="lightgreen").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Cerrar Archivo", command=cerrar_archivo, bg="lightcoral").grid(row=0, column=2, padx=5)

    frame_tabla = tk.Frame(ventana_editar)
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)


# ===========================================
# Ventana principal de prueba
# ===========================================
=======
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import openpyxl
import os

EXCEL_FILE = "inventario_lego.xlsx"

# ===========================================
# Crear el Excel si no existe
# ===========================================
if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    hoja = wb.active
    hoja.title = "Piezas"
    hoja.append(["ID Pieza", "Descripción", "Color", "Cantidad", "Set Origen", "Ubicación"])
    wb.save(EXCEL_FILE)


# ===========================================
# Ventana de edición del archivo
# ===========================================
def editar_archivo():
    ventana_editar = tk.Toplevel()
    ventana_editar.title("Editar Archivo - Inventario LEGO")
    ventana_editar.geometry("800x500")

    archivo_abierto = None
    df_actual = None
    tree = None

    # ----------------------------
    # Buscar archivo manualmente
    # ----------------------------
    def buscar_archivo():
        nonlocal archivo_abierto
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo Excel",
            filetypes=[("Archivos Excel", "*.xlsx *.xls")]
        )
        if ruta:
            archivo_abierto = ruta
            abrir_archivo()

    # ----------------------------
    # Abrir y mostrar archivo
    # ----------------------------
    def abrir_archivo():
        nonlocal df_actual, tree, archivo_abierto

        if not archivo_abierto:
            archivo_abierto = EXCEL_FILE

        try:
            df_actual = pd.read_excel(archivo_abierto)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")
            return

        # Limpiar tabla anterior
        for widget in frame_tabla.winfo_children():
            widget.destroy()

        # Crear tabla
        tree = ttk.Treeview(frame_tabla, columns=list(df_actual.columns), show="headings", height=15)
        for col in df_actual.columns:
            tree.heading(col, text=col)
            tree.column(col, width=120)
        for _, fila in df_actual.iterrows():
            tree.insert("", "end", values=list(fila))

        tree.pack(fill="both", expand=True)

        # Permitir doble clic en "Cantidad"
        tree.bind("<Double-1>", editar_celda)

    # ----------------------------
    # Editar celda (solo "Cantidad")
    # ----------------------------
    def editar_celda(event):
        nonlocal df_actual, tree

        item_id = tree.identify_row(event.y)
        col_id = tree.identify_column(event.x)
        if not item_id or not col_id:
            return

        col_index = int(col_id.replace("#", "")) - 1
        col_name = df_actual.columns[col_index]
        if col_name != "Cantidad":
            messagebox.showinfo("Edición no permitida", "Solo se puede modificar la columna 'Cantidad'.")
            return

        valores = tree.item(item_id, "values")
        valor_actual = valores[col_index]

        top = tk.Toplevel(ventana_editar)
        top.title("Editar cantidad")
        tk.Label(top, text=f"Cantidad actual: {valor_actual}").pack(pady=5)
        entrada = tk.Entry(top)
        entrada.insert(0, valor_actual)
        entrada.pack(pady=5)

        def confirmar():
            nuevo_valor = entrada.get()
            try:
                nuevo_valor = int(nuevo_valor)
            except ValueError:
                messagebox.showerror("Error", "Debe ser un número entero.")
                return

            # Actualizar DataFrame
            id_pieza = valores[0]
            idx = df_actual.index[df_actual["ID Pieza"] == id_pieza]
            if len(idx) == 0:
                messagebox.showerror("Error", "No se encontró el ID en el archivo.")
                top.destroy()
                return

            df_actual.loc[idx, "Cantidad"] = nuevo_valor
            df_actual.to_excel(archivo_abierto, index=False)

            # Actualizar tabla
            tree.item(item_id, values=tuple(
                nuevo_valor if i == col_index else v for i, v in enumerate(valores)
            ))

            top.destroy()
            messagebox.showinfo("Éxito", "Cantidad actualizada correctamente.")

        tk.Button(top, text="Guardar", command=confirmar).pack(pady=5)

    # ----------------------------
    # Cerrar archivo
    # ----------------------------
    def cerrar_archivo():
        nonlocal archivo_abierto, df_actual
        archivo_abierto = None
        df_actual = None
        for widget in frame_tabla.winfo_children():
            widget.destroy()
        messagebox.showinfo("Cerrar archivo", "Archivo cerrado correctamente.")

    # ----------------------------
    # Volver
    # ----------------------------
    def volver():
        ventana_editar.destroy()

    # ----------------------------
    # Interfaz gráfica
    # ----------------------------
    tk.Button(ventana_editar, text="⬅ Volver", command=volver, bg="#f0f0f0").pack(padx=10, pady=10, anchor="nw")

    frame_botones = tk.Frame(ventana_editar)
    frame_botones.pack(pady=5)

    tk.Button(frame_botones, text="Buscar Archivo", command=buscar_archivo, bg="lightblue").grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Abrir Archivo", command=abrir_archivo, bg="lightgreen").grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Cerrar Archivo", command=cerrar_archivo, bg="lightcoral").grid(row=0, column=2, padx=5)

    frame_tabla = tk.Frame(ventana_editar)
    frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)


# ===========================================
# Ventana principal de prueba
# ===========================================
>>>>>>> 2052878031b42032dedad2deecdbf8d74fafb595
