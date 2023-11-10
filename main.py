import tkinter as tki
from tkinter import Menu

# Die Liste der Funktionen und Datentypen sollte basierend auf den verfügbaren in Notion aktualisiert werden
functions_list = ["add", "subtract", "multiply", "if", ...] # usw.
datatypes_list = ["Number", "Text", "Date", "Boolean", ...] # usw.

class FormulaToolApp(tki.Tk):
    def __init__(self):
        super().__init__()

        self.title("Benutzerdefiniertes Formelwerkzeug")

        self.menu_bar = Menu(self)
        self.create_file_menu()
        self.create_functions_menu()
        self.create_datatypes_menu()
        self.config(menu=self.menu_bar)

        self.formula_text = tki.Text(self)
        self.formula_text.pack(fill=tki.BOTH, expand=True)

        self.preview_label = tki.Label(self, text="Vorschau:")
        self.preview_label.pack()

        self.preview_text = tki.Text(self, state=tki.DISABLED)
        self.preview_text.pack(fill=tki.BOTH, expand=True)

    def create_file_menu(self):
        file_menu = Menu(self.menu_bar)
        file_menu.add_command(label="Speichern", command=self.save_formula)
        file_menu.add_command(label="Laden", command=self.load_formula)
        file_menu.add_separator()
        file_menu.add_command(label="Beenden", command=self.quit)
        self.menu_bar.add_cascade(label="Datei", menu=file_menu)

    def create_functions_menu(self):
        functions_menu = Menu(self.menu_bar)
        for func in functions_list:
            functions_menu.add_command(label=func, command=lambda f=func: self.add_function_to_formula(f))
        self.menu_bar.add_cascade(label="Funktionen", menu=functions_menu)

    def create_datatypes_menu(self):
        datatypes_menu = Menu(self.menu_bar)
        for datatype in datatypes_list:
            datatypes_menu.add_command(label=datatype, command=lambda dt=datatype: self.add_datatype_to_formula(dt))
        self.menu_bar.add_cascade(label="Datentypen", menu=datatypes_menu)

    def add_function_to_formula(self, function_name):
        # Logik zum Hinzufügen der Funktion zur Formel
        pass

    def add_datatype_to_formula(self, datatype_name):
        # Logik zum Hinzufügen des Datentyps zur Formel
        pass

    def save_formula(self):
        # Implementierung zum Speichern der Formel
        pass

    def load_formula(self):
        # Implementierung zum Laden einer Formel
        pass

# Hauptprogramm
if __name__ == "__main__":
    app = FormulaToolApp()
    app.mainloop()
