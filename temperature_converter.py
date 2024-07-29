
import tkinter as tk
from tkinter import ttk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        label_result.config(text="Invalid input")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Invalid input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the Celsius input widgets
label_celsius = ttk.Label(root, text="Celsius:")
label_celsius.grid(column=0, row=0, padx=10, pady=10)
entry_celsius = ttk.Entry(root)
entry_celsius.grid(column=1, row=0, padx=10, pady=10)
button_celsius = ttk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_celsius.grid(column=2, row=0, padx=10, pady=10)

# Create and place the Fahrenheit input widgets
label_fahrenheit = ttk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(column=0, row=1, padx=10, pady=10)
entry_fahrenheit = ttk.Entry(root)
entry_fahrenheit.grid(column=1, row=1, padx=10, pady=10)
button_fahrenheit = ttk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_fahrenheit.grid(column=2, row=1, padx=10, pady=10)

# Create and place the result label
label_result = ttk.Label(root, text="Result:")
label_result.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

# Run the application
root.mainloop()