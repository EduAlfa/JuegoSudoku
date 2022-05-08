
from tkinter import ttk
from tkinter import *
#Generando la tabla desde 0 estableciendo valores definidos y no aleatorias hacia los elementos de la matriz
tablero = [
    [0, 0, 5, 0, 2, 0, 0, 0, 8],
    [8, 0, 2, 0, 0, 9, 0, 6, 0],
    [0, 0, 3, 8, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 3, 0, 4, 0],
    [0, 0, 0, 2, 7, 0, 0, 0, 0],
    [4, 9, 0, 0, 6, 2, 0, 7, 0],
    [0, 0, 0, 0, 9, 4, 6, 1, 2],
    [2, 0, 6, 0, 0, 8, 3, 0, 4]
]

#Función que mostrará el tablero en pantalla
def mostrarTablero(tablero):
    for i in range(len(tablero)):
        if i % 3 == 0 and i != 0:
            
        for j in range(len(tablero[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")


#Función encargada de encontrar los espacios que se encuentren disponibles 

def hallarVacio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 0:
                return i, j
    return None


#Función encargada de ingresar los números faltantes


def resolver(tablero):
    find = hallarVacio(tablero)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validar(tablero, i, (row, col)):
            tablero[row][col] = i

            if resolver(tablero):
                return True

            tablero[row][col] = 0

    return False


#Función encargada de validar que los números se estén ingresando en las posiciones correctas

def validar(tablero, numero, posicion):
    if (checkFila(tablero, numero, posicion) and
            checkCol(tablero, numero, posicion) and
            revisionCuadro(tablero, numero, posicion)):
        return True
    return False


#Función encargada de verificar las filas de la matriz


def checkFila(tablero, numero, posicion):
    for i in range(len(tablero[0])):
        if tablero[posicion[0]][i] == numero and posicion[1] != i:
            return False
    return True


#Función encargada de verificar las columnas de la matriz

def checkCol(tablero, numero, posicion):
    for i in range(len(tablero)):
        if tablero[i][posicion[1]] == numero and posicion[0] != i:
            return False
    return True

#Función encargada de verificar los cuadrados de 3x3

def revisionCuadro(tablero, numero, posicion):
    cuadro_x = posicion[1] // 3
    cuadro_y = posicion[0] // 3

    for i in range(cuadro_y * 3, cuadro_y * 3 + 3):
        for j in range(cuadro_x * 3, cuadro_x * 3 + 3):
            if tablero[i][j] == numero and (i, j) != posicion:
                return False
    return True


def play(tablero):
    root = Tk() # Creando la ventana principal
    root.geometry("400x400")# Tamaño de la ventana
    root.maxsize(400, 400)
    root.minsize(400, 400)
    root.title("Sudoku")#Titulo de la ventana
    for i in range(9):
        for j in range(9):
            entry = ttk.Entry(root, width=2, font=("Courier", 20))
            entry.grid(row=i, column=j, padx=1, pady=1)
            entry.insert(0, tablero[i][j])
            if tablero[i][j] != 0:
                entry.config(state="disabled")

# Creando el boton para ingresar el número
    boton = ttk.Button(root, text="Resolver")
    boton.grid(row=9, column=0, columnspan=9, pady=1)
# Iniciar la ventana
    root.mainloop()

#Corriendo la interfaz
play(tablero)
