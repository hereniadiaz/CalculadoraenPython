from tkinter import *
root = Tk()
root.title("CALCULADORA")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0
def agregar_num(n):
    global i
    display.insert(i, n)
    i += 1

def operaciones(operator):
    global i
    operador_longitud = len(operator)
    display.insert(i, operator)
    i += operador_longitud

def limpiar():
    display.delete(0, END)

def borrar_de_uno():
    estado_pantalla = display.get()
    if len(estado_pantalla):
        nuevo_estado = estado_pantalla[:-1]
        limpiar()
        display.insert(0, nuevo_estado)
    else:
        limpiar()
        display.insert(0, 'Error')

def calcular():
    estado_pantalla = display.get()
    try:
        expresion_matematica = compile(estado_pantalla, 'app.py', 'eval')
        resultado = eval(expresion_matematica)
        limpiar()
        display.insert(0, resultado)
    except:
        limpiar()
        display.insert(0, "Error")

Button(root, text="1", command=lambda:agregar_num(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:agregar_num(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:agregar_num(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:agregar_num(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:agregar_num(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:agregar_num(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:agregar_num(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:agregar_num(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:agregar_num(9)).grid(row=4, column=2, sticky=W+E)

Button(root, text="0", command=lambda:agregar_num(0)).grid(row=5, column=1, sticky=W+E)

Button(root, text="AC", command=lambda:limpiar()).grid(row=5, column=0, sticky=W+E)
Button(root, text="←", command=lambda:borrar_de_uno()).grid(row=2, column=4, sticky=W+E, columnspan=2)

Button(root, text="%", command=lambda:operaciones("%")).grid(row=5, column=2, sticky=W+E)
Button(root, text="+", command=lambda:operaciones("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:operaciones("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:operaciones("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:operaciones("/")).grid(row=5, column=3, sticky=W+E)
Button(root, text="exp", command=lambda:operaciones("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="˄2", command=lambda:operaciones("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda:operaciones("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda:operaciones(")")).grid(row=4, column=5, sticky=W+E)

Button(root, text="=", command=lambda:calcular()).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()
