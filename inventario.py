import tkinter as tk
from modo_manual import abrir_modo_manual
from modo_visual import abrir_modo_visual
from editar_archivo import editar_archivo
root = tk.Tk()
root.title("Inventario LEGO - Inicio")
root.geometry("400x285")

tk.Label(root, text="Bienvenido al Inventario LEGO", font=("Arial", 14, "bold")).pack(pady=30)
tk.Button(root, text="🧠 Modo Manual", command=abrir_modo_manual, bg="lightblue", width=20, height=2).pack(pady=10)
tk.Button(root, text="🖼️ Modo Visual", command=abrir_modo_visual, bg="lightgreen", width=20, height=2).pack(pady=10)
tk.Button(root, text="✏️ Editar Archivo", command=editar_archivo, bg="lightyellow", width=20, height=2).pack(pady=10)
root.mainloop()
