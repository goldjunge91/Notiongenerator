import tkinter as tk

# Wörterbuch zur Speicherung von Notion-Funktionen und -Typen
notion_functions = {
    "concat": "concat(value1, value2)",
    "trim": "trim(value)",
    # Weitere Funktionen hier hinzufügen...
}

notion_types = {
    "text": "text",
    "number": "number",
    # Weitere Typen hier hinzufügen...
}

def generate_formula():
    function = function_dropdown.get()
    type_ = type_dropdown.get()
    expression = formula_entry.get()

    formula = f"{function}({expression})"
    result_label.config(text=formula)

# GUI erstellen
root = tk.Tk()

# Dropdown-Menü für Funktionen
function_label = tk.Label(root, text="Funktion:")
function_label.pack()

function_dropdown = tk.OptionMenu(root, *notion_functions.keys())
function_dropdown.pack()

# Dropdown-Menü für Typen
type_label = tk.Label(root, text="Typ:")
type_label.pack()

type_dropdown = tk.OptionMenu(root, *notion_types.keys())
type_dropdown.pack()

# Eingabefeld für Formelausdrücke
formula_label = tk.Label(root, text="Formel:")
formula_label.pack()

formula_entry = tk.Entry(root)
formula_entry.pack()

# Schaltfläche zum Generieren der Formel
generate_button = tk.Button(root, text="Formel generieren", command=generate_formula)
generate_button.pack()

# Ergebnislabel
result_label = tk.Label(root, text="")
result_label.pack()

# Tkinter-Ereignisschleife ausführen
root.mainloop()
