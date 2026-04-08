import tkinter as tk
from interfaz import iniciar_programa

def setup_interfaz():
    #ventana principal
    ventana = tk.Tk()
    ventana.title("Visualizador de Metodos de Ordenamiento")
    ventana.geometry("800x600")
    ventana.config(bg="#2c3e50")

    #menu principal
    frame_menu = tk.Frame(ventana, bg="#e41212")
    frame_menu.pack(fill="both", expand=True)

    tk.Label(frame_menu, text="Interfaz Grafica de los Metodos de Ordenamiento", font=("Arial", 18, "bold"), bg="#482c50", fg="white").pack(pady=30)

    #seleccion de metodo
    tk.Label(frame_menu, text="1. Selecciona el metodo de ordenamiento:", font=("Arial", 12), bg="#462c50", fg="white").pack(pady=5)
    var_metodo = tk.StringVar(value="Bubble Sort")
    metodos = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
    frame_radios_metodo = tk.Frame(frame_menu, bg="#482c50")
    frame_radios_metodo.pack(pady=5)
    for m in metodos:
        tk.Radiobutton(frame_radios_metodo, text=m, variable=var_metodo, value=m, bg="#482c50", fg="white", selectcolor="#482c50", font=("Arial", 11)).pack(side="left", padx=10)

    #tamaño de la lista
    tk.Label(frame_menu, text="2. ¿De que tamaño debe ser la lista? (Rango sugerido: 5 - 600):", font=("Arial", 12), bg="#482c50", fg="white").pack(pady=20)
    entry_tamano = tk.Entry(frame_menu, font=("Arial", 12), width=10, justify="center")
    entry_tamano.insert(0, "30") #Tamaño por defecto
    entry_tamano.pack()

    #velocidad
    tk.Label(frame_menu, text="3. Selecciona la velocidad de los movimientos:", font=("Arial", 12), bg="#482c50", fg="white").pack(pady=20)
    var_velocidad = tk.StringVar(value="rapida")
    velocidades = [("Lenta", "lenta"), ("Media", "media"), ("Rápida", "rapida")]
    frame_radios_vel = tk.Frame(frame_menu, bg="#482c50")
    frame_radios_vel.pack(pady=5)
    for text, val in velocidades:
        tk.Radiobutton(frame_radios_vel, text=text, variable=var_velocidad, value=val, bg="#482c50", fg="white", selectcolor="#34495e", font=("Arial", 11)).pack(side="left", padx=10)

    #histograma
    frame_canvas = tk.Frame(ventana, bg="#482c50")
    canvas = tk.Canvas(frame_canvas, width=700, height=400, bg="white", highlightthickness=2, highlightbackground="#482c50")
    canvas.pack(pady=50)

    #boton Iniciar
    btn_iniciar = tk.Button(frame_menu, text="COMENZAR ORDENAMIENTO", font=("Arial", 14, "bold"), bg="#a0ae27", fg="white", command=lambda: iniciar_programa(frame_menu, frame_canvas, entry_tamano, var_metodo, var_velocidad, ventana, canvas), cursor="hand2", padx=20, pady=10)
    btn_iniciar.pack(pady=40)

    return ventana