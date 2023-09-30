import random
import tkinter as tk
from tkinter import Label, Entry, Button

def estimate_pi(num_points):
    inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        distance = (x - 0.5)**2 + (y - 0.5)**2

        if distance <= 0.25:
            inside_circle += 1

    pi_estimate = (inside_circle / total_points) * 4
    return pi_estimate

def calculate_pi():
    num_points = int(entry.get())
    pi_value = estimate_pi(num_points)
    result_label.config(text=f"Estimación de Pi: {pi_value}")

# Configuración de la ventana
window = tk.Tk()
window.title("Estimador de Pi")

# Etiqueta y entrada para el número de puntos
label = Label(window, text="Número de puntos:")
label.pack()
entry = Entry(window)
entry.pack()

# Botón para calcular Pi
calculate_button = Button(window, text="Calcular Pi", command=calculate_pi)
calculate_button.pack()

# Etiqueta para mostrar el resultado
result_label = Label(window, text="")
result_label.pack()

# Ejecutar la ventana
window.mainloop()
