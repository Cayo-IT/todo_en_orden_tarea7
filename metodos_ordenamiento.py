import time

#insertion_sort
def insertion_sort(self, dibujar_funcion, pausa):
    moves = 0
    for i in range(0, self.size):
        for j in range(i, 0, -1):
            if self[j] < self[j-1]:
                self.swap(j, j-1)
                moves += 1
                dibujar_funcion(self)
                time.sleep(pausa)
            else:
                break
    return moves

#merge_sort
def merge_sort(self, dibujar_funcion, pausa, start=0, end=None, moves=None):
    if moves is None:
        moves = [0]
    if end is None:
        end = self.size 
    if end - start <= 1:
        return moves[0]
        
    mid = (start + end) // 2
    self.merge_sort(dibujar_funcion, pausa, start, mid, moves) #ordenar la lista izquierda
    self.merge_sort(dibujar_funcion, pausa, mid, end, moves)   #ordenar la lista derecha
    
    #extraer los valores para unirlos
    left = [self[x] for x in range(start, mid)]
    right = [self[x] for x in range(mid, end)]
    
    i = j = 0
    k = start
    #unir listas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            self[k] = left[i]
            i += 1
        else:
            self[k] = right[j]
            j += 1
        moves[0] += 1
        dibujar_funcion(self)
        time.sleep(pausa)
        k += 1
        
    while i < len(left):
        self[k] = left[i]
        i += 1
        k += 1
        moves[0] += 1
        dibujar_funcion(self)
        time.sleep(pausa)
        
    while j < len(right):
        self[k] = right[j]
        j += 1
        k += 1
        moves[0] += 1
        dibujar_funcion(self)
        time.sleep(pausa)
        
    return moves[0]

#quick_sort
def partition(self, start, end, dibujar_funcion, pausa, moves):
    pivote = self[end]
    i = start - 1
    for j in range(start, end):
        if self[j] <= pivote:
            i += 1
            self.swap(i, j)
            moves[0] += 1
            dibujar_funcion(self)
            time.sleep(pausa)
    self.swap(i + 1, end)
    moves[0] += 1
    dibujar_funcion(self)
    time.sleep(pausa)
    return i + 1

def quick_sort(self, dibujar_funcion, pausa, start=0, end=None, moves=None):
    if moves is None:
        moves = [0]
    if end is None:
        end = self.size - 1
    if start < end:
        pivote = self.partition(start, end, dibujar_funcion, pausa, moves)
        self.quick_sort(dibujar_funcion, pausa, start, pivote - 1, moves)
        self.quick_sort(dibujar_funcion, pausa, pivote + 1, end, moves)
    return moves[0]