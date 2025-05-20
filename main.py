import random
import string
import customtkinter as ctk
import pyperclip
import sys

# Verificar que estamos en el entorno virtual correcto
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")

# Modo de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Lista de símbolos seguros y variados
simbolos = list(string.ascii_letters + string.digits + "-/.*@#!&%$+?^()<>;ñÑ")

class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.title("Generador de Contraseñas 🔐")
        self.geometry("500x600")
        self.resizable(False, False)

        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.titulo = ctk.CTkLabel(
            self.frame, 
            text="Generador de Contraseñas", 
            font=("Helvetica", 24, "bold")
        )
        self.titulo.pack(pady=20)

        # Opciones de longitud
        self.opciones_frame = ctk.CTkFrame(self.frame)
        self.opciones_frame.pack(pady=10, padx=20, fill="x")

        self.opcion_var = ctk.StringVar(value="1")
        
        opciones = [
            ("Corta / poco segura 🥱 (7 caracteres)", "1"),
            ("Mediana / moderadamente segura 🥸 (11 caracteres)", "2"),
            ("Larga / muy segura 🔒 (20 caracteres)", "3"),
            ("Personalizada 🤯", "4")
        ]

        for texto, valor in opciones:
            ctk.CTkRadioButton(
                self.opciones_frame,
                text=texto,
                variable=self.opcion_var,
                value=valor,
                command=self.actualizar_longitud_personalizada
            ).pack(pady=5, padx=10, anchor="w")

        # Entrada para longitud personalizada
        self.longitud_frame = ctk.CTkFrame(self.frame)
        self.longitud_frame.pack(pady=10, padx=20, fill="x")
        
        self.longitud_label = ctk.CTkLabel(
            self.longitud_frame,
            text="Longitud personalizada:",
            font=("Helvetica", 12)
        )
        self.longitud_label.pack(side="left", padx=10)
        
        self.longitud_entry = ctk.CTkEntry(
            self.longitud_frame,
            width=100,
            state="disabled"
        )
        self.longitud_entry.pack(side="left", padx=10)

        # Botón para generar contraseña
        self.generar_btn = ctk.CTkButton(
            self.frame,
            text="Generar Contraseña 🔑",
            command=self.generar_password,
            font=("Helvetica", 14, "bold")
        )
        self.generar_btn.pack(pady=20)

        # Frame para mostrar la contraseña
        self.password_frame = ctk.CTkFrame(self.frame)
        self.password_frame.pack(pady=10, padx=20, fill="x")
        
        self.password_label = ctk.CTkLabel(
            self.password_frame,
            text="Tu contraseña aparecerá aquí",
            font=("Helvetica", 14)
        )
        self.password_label.pack(pady=10)

        # Botones de acción
        self.acciones_frame = ctk.CTkFrame(self.frame)
        self.acciones_frame.pack(pady=10, padx=20, fill="x")

        self.copiar_btn = ctk.CTkButton(
            self.acciones_frame,
            text="Copiar al Portapapeles 📋",
            command=self.copiar_password,
            state="disabled"
        )
        self.copiar_btn.pack(side="left", padx=5, expand=True)

        self.guardar_btn = ctk.CTkButton(
            self.acciones_frame,
            text="Guardar en Archivo 💾",
            command=self.guardar_password,
            state="disabled"
        )
        self.guardar_btn.pack(side="left", padx=5, expand=True)

    def actualizar_longitud_personalizada(self):
        if self.opcion_var.get() == "4":
            self.longitud_entry.configure(state="normal")
        else:
            self.longitud_entry.configure(state="disabled")

    def generar_password(self):
        opcion = self.opcion_var.get()
        
        if opcion == "1":
            cantidad = 7
        elif opcion == "2":
            cantidad = 11
        elif opcion == "3":
            cantidad = 20
        else:
            try:
                cantidad = int(self.longitud_entry.get())
                if cantidad <= 0:
                    self.mostrar_error("La longitud debe ser mayor a cero")
                    return
            except ValueError:
                self.mostrar_error("Por favor ingresa un número válido")
                return

        self.password = ''.join(random.choice(simbolos) for _ in range(cantidad))
        self.password_label.configure(text=self.password)
        self.copiar_btn.configure(state="normal")
        self.guardar_btn.configure(state="normal")

    def copiar_password(self):
        try:
            pyperclip.copy(self.password)
            self.mostrar_mensaje("Contraseña copiada al portapapeles")
        except Exception as e:
            print(f"Error al copiar: {str(e)}")
            self.mostrar_error(f"Error al copiar: {str(e)}")

    def guardar_password(self):
        try:
            with open("contraseña.txt", "w", encoding="utf-8") as archivo:
                archivo.write(self.password)
            self.mostrar_mensaje("Contraseña guardada en contraseña.txt")
        except Exception as e:
            print(f"Error al guardar: {str(e)}")
            self.mostrar_error(f"Error al guardar: {str(e)}")

    def mostrar_mensaje(self, mensaje):
        dialog = ctk.CTkInputDialog(
            text=mensaje,
            title="Mensaje",
            button_text="OK"
        )
        dialog.destroy()

    def mostrar_error(self, mensaje):
        dialog = ctk.CTkInputDialog(
            text=mensaje,
            title="Error",
            button_text="OK"
        )
        dialog.destroy()

if __name__ == "__main__":
    try:
        app = PasswordGenerator()
        app.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {str(e)}")
        input("Presiona Enter para salir...")