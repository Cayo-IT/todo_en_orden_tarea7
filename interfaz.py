#librerias
import tkinter as tk
from tkinter import messagebox
import random
import time
from Llist import llist

#InterfazGrafica
def dibujar_histograma(lista, ventana, canvas):
    canvas.delete("all")
    if lista.size == 0: return
    ancho_canvas = 700
    alto_canvas = 400
    ancho_barra = ancho_canvas / lista.size
    
    max_val = max([lista[i] for i in range(lista.size)]) if lista.size > 0 else 1
    
    for i in range(lista.size):
        valor = lista[i]
        x_izq = i * ancho_barra
        #ae escala el tamaño de las barras en relación al alto del canvas
        y_arriba = alto_canvas - ((valor / max_val) * (alto_canvas - 20))
        x_der = (i + 1) * ancho_barra
        y_abajo = alto_canvas
        
        canvas.create_rectangle(x_izq, y_arriba, x_der, y_abajo, fill="blue", outline="black")
    
    ventana.update()

def iniciar_programa(frame_menu, frame_canvas, entry_tamano, var_metodo, var_velocidad, ventana, canvas):
    try:
        tamano = int(entry_tamano.get())
        if tamano < 5 or tamano > 600:
            messagebox.showwarning("Tamaño invalido", "Ingresa un tamaño entre 5 y 600 para la visualizacion.")
            return
    except ValueError:
        messagebox.showwarning("Entrada invalida", "Ingresa un numero entero valido.")
        return
        
    metodo = var_metodo.get()
    if not metodo:
        messagebox.showwarning("Metodo faltante", "Selecciona un método de ordenamiento.")
        return
        
    vel = var_velocidad.get()
    if vel == "lenta":
        pausa = 0.3
    elif vel == "media":
        pausa = 0.05
    else:
        pausa = 0.01

    #cambiar de imagen (Ocultar menu y mostrar histograma)
    frame_menu.pack_forget()
    frame_canvas.pack(fill="both", expand=True)
    
    #crear y llenar lista de manera aleatoria
    mi_lista = llist()
    for _ in range(tamano):
        mi_lista.append(random.randint(10, 100))

    dibujar_hist_lambda = lambda lista : dibujar_histograma(lista, ventana, canvas)
        
    #dibujar estado inicial
    dibujar_hist_lambda(mi_lista)
    time.sleep(1.0)
    
    #ejecutar algoritmo de ordenamiento
    moves = 0
    if metodo == "Bubble Sort":
        moves = mi_lista.bubble_sort(dibujar_hist_lambda, pausa)
    elif metodo == "Selection Sort":
        moves = mi_lista.selection_sort(dibujar_hist_lambda, pausa)
    elif metodo == "Insertion Sort":
        moves = mi_lista.insertion_sort(dibujar_hist_lambda, pausa)
    elif metodo == "Merge Sort":
        moves = mi_lista.merge_sort(dibujar_hist_lambda, pausa)
    elif metodo == "Quick Sort":
        moves = mi_lista.quick_sort(dibujar_hist_lambda, pausa)
        
    dibujar_hist_lambda(mi_lista)
    
    #preguntar al usuario si reiniciar o salir
    respuesta = messagebox.askyesno(
        "Ordenamiento Terminado!",
        f"La lista se ha ordenado completamente.\nTomo un total de {moves} movimientos.\n\nDeseas regresar al menu principal?")
    
    if respuesta:
        frame_canvas.pack_forget()
        frame_menu.pack(fill="both", expand=True)
    else:
        ventana.destroy()
