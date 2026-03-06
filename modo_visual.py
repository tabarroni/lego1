<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pandas as pd
from funciones_excel import agregar_a_excel

# 📁 Carpeta local de imágenes
IMAGES_DIR = r"E:\mi_proyecto\piezas"  

# 📂 Cargar datos desde CSV
CSV_FILE = "piezas_lego.csv"
df_piezas = pd.read_csv(CSV_FILE)
piezas = df_piezas.to_dict(orient="records")

def abrir_modo_visual():
    ventana_visual = tk.Toplevel()
    ventana_visual.title("Modo Visual - Inventario LEGO")
    ventana_visual.geometry("1200x760")

    # ===== Botón para volver =====
    def volver():
        ventana_visual.destroy()  # cierra esta ventana y regresa a la anterior

    tk.Button(ventana_visual, text="⬅ Volver", command=volver, bg="#f0f0f0").pack(padx=10, pady=10, anchor="nw")

    # ===== Panel principal =====
    frame_principal = tk.Frame(ventana_visual)
    frame_principal.pack(fill="both", expand=True)

    # ===== Panel izquierdo (buscador) =====
    frame_filtros = tk.Frame(frame_principal, padx=10, pady=10, bg="#f2f2f2")
    frame_filtros.pack(side="left", fill="y")

    tk.Label(frame_filtros, text="🔍 Buscar por nombre o ID:", bg="#f2f2f2", font=("Arial", 12, "bold")).pack(anchor="w")
    entry_buscar = tk.Entry(frame_filtros, width=25)
    entry_buscar.pack(anchor="w", pady=5)

    # ===== Panel derecho (grilla de piezas) =====
    frame_grilla = tk.Frame(frame_principal)
    frame_grilla.pack(side="right", fill="both", expand=True)

    canvas = tk.Canvas(frame_grilla)
    scrollbar = ttk.Scrollbar(frame_grilla, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ===== Mostrar piezas =====
    def mostrar_piezas(lista):
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        columnas = 6
        MAX_PIEZAS = 100  # solo muestra 100 al inicio

        def cargar_pieza(i):
            if i >= min(len(lista), MAX_PIEZAS):
                return
            pieza = lista[i]
            frame = ttk.Frame(scrollable_frame, borderwidth=1, relief="ridge", padding=8)
            frame.grid(row=i // columnas, column=i % columnas, padx=5, pady=5)

            id_pieza = str(pieza["id"])
            nombre = pieza["descripcion"]

            # === Cargar imagen desde carpeta local ===
            ruta_local = os.path.join(IMAGES_DIR, f"{id_pieza}.jpg")
            if os.path.exists(ruta_local):
                try:
                    img = Image.open(ruta_local).resize((90, 90))
                    photo = ImageTk.PhotoImage(img)
                    lbl_img = tk.Label(frame, image=photo)
                    lbl_img.image = photo
                    lbl_img.pack()
                except Exception:
                    tk.Label(frame, text="(error al cargar imagen)").pack()
            else:
                tk.Label(frame, text="(sin imagen)").pack()

            # === Texto ===
            tk.Label(frame, text=nombre, wraplength=100, justify="center").pack(pady=2)
            tk.Label(frame, text=f"ID: {id_pieza}", fg="gray").pack()

            # === Botón agregar ===
            def agregar_p(p=pieza):
                # Crear ventana emergente para ingresar cantidad
                ventana_cant = tk.Toplevel(ventana_visual)
                ventana_cant.title("Agregar cantidad")
                ventana_cant.geometry("300x150")
                ventana_cant.resizable(False, False)

                tk.Label(ventana_cant, text=f"Pieza: {p['descripcion']}", wraplength=250, font=("Arial", 10, "bold")).pack(pady=10)
                tk.Label(ventana_cant, text="Ingrese cantidad:").pack()

                entry_cant = tk.Entry(ventana_cant, width=10, justify="center")
                entry_cant.insert(0, "1")
                entry_cant.pack(pady=5)

                # Función para confirmar cantidad
                def confirmar():
                    try:
                        cantidad = int(entry_cant.get())
                        if cantidad <= 0:
                            raise ValueError
                    except ValueError:
                        messagebox.showerror("Error", "Ingrese una cantidad válida (entero positivo).")
                        return

                    # Llamar función original con la cantidad ingresada
                    agregar_a_excel(p["id"], p["descripcion"], "", cantidad, "", "")
                    ventana_cant.destroy()
                    messagebox.showinfo("Agregado", f"Se agregaron {cantidad} unidades de '{p['descripcion']}'.")

                tk.Button(ventana_cant, text="Confirmar", command=confirmar, bg="lightgreen").pack(pady=10)
                tk.Button(ventana_cant, text="Cancelar", command=ventana_cant.destroy, bg="lightgray").pack()

            tk.Button(frame, text="Agregar", command=agregar_p, bg="lightgreen").pack(pady=3)

            # Cargar siguiente pieza sin bloquear
            ventana_visual.after(1, lambda: cargar_pieza(i + 1))

        cargar_pieza(0)

    # ===== Filtro búsqueda =====
    def actualizar_grilla():
        texto = entry_buscar.get().strip().lower()
        if not texto:
            lista_filtrada = piezas
        else:
            lista_filtrada = [
                p for p in piezas
                if texto in str(p["id"]).lower() or texto in str(p["descripcion"]).lower()
            ]
        mostrar_piezas(lista_filtrada)

    entry_buscar.bind("<KeyRelease>", lambda e: actualizar_grilla())

    # ===== Mostrar todas al inicio =====
    mostrar_piezas(piezas)
=======
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import pandas as pd
from funciones_excel import agregar_a_excel

# 📁 Carpeta local de imágenes
IMAGES_DIR = r"E:\mi_proyecto\piezas"  

# 📂 Cargar datos desde CSV
CSV_FILE = "piezas_lego.csv"
df_piezas = pd.read_csv(CSV_FILE)
piezas = df_piezas.to_dict(orient="records")

def abrir_modo_visual():
    ventana_visual = tk.Toplevel()
    ventana_visual.title("Modo Visual - Inventario LEGO")
    ventana_visual.geometry("1200x760")

    # ===== Botón para volver =====
    def volver():
        ventana_visual.destroy()  # cierra esta ventana y regresa a la anterior

    tk.Button(ventana_visual, text="⬅ Volver", command=volver, bg="#f0f0f0").pack(padx=10, pady=10, anchor="nw")

    # ===== Panel principal =====
    frame_principal = tk.Frame(ventana_visual)
    frame_principal.pack(fill="both", expand=True)

    # ===== Panel izquierdo (buscador) =====
    frame_filtros = tk.Frame(frame_principal, padx=10, pady=10, bg="#f2f2f2")
    frame_filtros.pack(side="left", fill="y")

    tk.Label(frame_filtros, text="🔍 Buscar por nombre o ID:", bg="#f2f2f2", font=("Arial", 12, "bold")).pack(anchor="w")
    entry_buscar = tk.Entry(frame_filtros, width=25)
    entry_buscar.pack(anchor="w", pady=5)

    # ===== Panel derecho (grilla de piezas) =====
    frame_grilla = tk.Frame(frame_principal)
    frame_grilla.pack(side="right", fill="both", expand=True)

    canvas = tk.Canvas(frame_grilla)
    scrollbar = ttk.Scrollbar(frame_grilla, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # ===== Mostrar piezas =====
    def mostrar_piezas(lista):
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        columnas = 6
        MAX_PIEZAS = 100  # solo muestra 100 al inicio

        def cargar_pieza(i):
            if i >= min(len(lista), MAX_PIEZAS):
                return
            pieza = lista[i]
            frame = ttk.Frame(scrollable_frame, borderwidth=1, relief="ridge", padding=8)
            frame.grid(row=i // columnas, column=i % columnas, padx=5, pady=5)

            id_pieza = str(pieza["id"])
            nombre = pieza["descripcion"]

            # === Cargar imagen desde carpeta local ===
            ruta_local = os.path.join(IMAGES_DIR, f"{id_pieza}.jpg")
            if os.path.exists(ruta_local):
                try:
                    img = Image.open(ruta_local).resize((90, 90))
                    photo = ImageTk.PhotoImage(img)
                    lbl_img = tk.Label(frame, image=photo)
                    lbl_img.image = photo
                    lbl_img.pack()
                except Exception:
                    tk.Label(frame, text="(error al cargar imagen)").pack()
            else:
                tk.Label(frame, text="(sin imagen)").pack()

            # === Texto ===
            tk.Label(frame, text=nombre, wraplength=100, justify="center").pack(pady=2)
            tk.Label(frame, text=f"ID: {id_pieza}", fg="gray").pack()

            # === Botón agregar ===
            def agregar_p(p=pieza):
                # Crear ventana emergente para ingresar cantidad
                ventana_cant = tk.Toplevel(ventana_visual)
                ventana_cant.title("Agregar cantidad")
                ventana_cant.geometry("300x150")
                ventana_cant.resizable(False, False)

                tk.Label(ventana_cant, text=f"Pieza: {p['descripcion']}", wraplength=250, font=("Arial", 10, "bold")).pack(pady=10)
                tk.Label(ventana_cant, text="Ingrese cantidad:").pack()

                entry_cant = tk.Entry(ventana_cant, width=10, justify="center")
                entry_cant.insert(0, "1")
                entry_cant.pack(pady=5)

                # Función para confirmar cantidad
                def confirmar():
                    try:
                        cantidad = int(entry_cant.get())
                        if cantidad <= 0:
                            raise ValueError
                    except ValueError:
                        messagebox.showerror("Error", "Ingrese una cantidad válida (entero positivo).")
                        return

                    # Llamar función original con la cantidad ingresada
                    agregar_a_excel(p["id"], p["descripcion"], "", cantidad, "", "")
                    ventana_cant.destroy()
                    messagebox.showinfo("Agregado", f"Se agregaron {cantidad} unidades de '{p['descripcion']}'.")

                tk.Button(ventana_cant, text="Confirmar", command=confirmar, bg="lightgreen").pack(pady=10)
                tk.Button(ventana_cant, text="Cancelar", command=ventana_cant.destroy, bg="lightgray").pack()

            tk.Button(frame, text="Agregar", command=agregar_p, bg="lightgreen").pack(pady=3)

            # Cargar siguiente pieza sin bloquear
            ventana_visual.after(1, lambda: cargar_pieza(i + 1))

        cargar_pieza(0)

    # ===== Filtro búsqueda =====
    def actualizar_grilla():
        texto = entry_buscar.get().strip().lower()
        if not texto:
            lista_filtrada = piezas
        else:
            lista_filtrada = [
                p for p in piezas
                if texto in str(p["id"]).lower() or texto in str(p["descripcion"]).lower()
            ]
        mostrar_piezas(lista_filtrada)

    entry_buscar.bind("<KeyRelease>", lambda e: actualizar_grilla())

    # ===== Mostrar todas al inicio =====
    mostrar_piezas(piezas)
>>>>>>> 2052878031b42032dedad2deecdbf8d74fafb595
