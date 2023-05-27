from cgitb import enable
from tkinter import *
from tkinter import ttk
from tkinter.font import Font


# Funcion que valida la palabra
def validarPalabra(transiciones, estadoInicial, indicacion, palabraDeEntrada, estadoFinal=None):
    size = len(palabraDeEntrada)
    estadoReal = estadoInicial
    estadoPila = "R"
    pila = "R"
    listaAcomparar = [estadoInicial, palabraDeEntrada[0], estadoPila]

    validarLenguaje = False
    for j in palabraDeEntrada:
        validarLenguaje = False
        for i in transiciones:
            if j== i[1]:
                validarLenguaje = True
        if not(validarLenguaje):
            return False


    contador = 0
    for j in range(size):
        listaAcomparar = [estadoReal, palabraDeEntrada[j], estadoPila]
        #print(f'pila: {pila}\n Accion Pila: {estadoPila}\n estadoReal: {estadoReal},\n caracter: {palabraDeEntrada[j]}')
        for i in transiciones:

            if i == tuple(listaAcomparar):
                #print(f'pila: {pila}\n Accion Pila: {estadoPila}\n estadoReal: {estadoReal},\n caracter: {palabraDeEntrada[j]}')
                contador += 1
                estadoReal = transiciones.get(i)[0]
                estadoPila = transiciones.get(i)[1][0]
                if estadoPila == "e":
                    pila = pila[1::]
                    if (len(pila)== 0 and contador==size):
                        return True
                    if (len(pila)!=0):
                        estadoPila = pila[0]
                    # print(estadoPila)
                else:
                    #print(f"pilaGeneral: {transiciones.get(i)[1][0:len(transiciones.get(i)[1])-1]} \n")
                    x = len(transiciones.get(i)[1])-1
                    if x > 0:
                        pila = transiciones.get(i)[1][0:x] + pila
    #print(f"estadoReal: {estadoReal} \n pila: {pila}\n")
    if contador!= size:
        return False
    print(contador)
    if indicacion:
        if estadoFinal == estadoReal:
            return True
        else:
            return False
    else:
        if len(pila) == 0:
            return True
        else:
            return False


# Crear app
App = Tk()
# Asignar titulo
App.title("Autómata PushDown Determinista")
anchoVentana = 800
altoVentana = 450
#Calculo para centrar la ventana
x_ventana = App.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = App.winfo_screenheight() // 2 - altoVentana // 2
posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
App.geometry(posicion)
App.resizable(False, False)

#Variable de Validación
palabraValidada = BooleanVar()
#Crear Ventana de Palabra Aceptada -> o denegada
def openNewWindow():
    newWindow = Toplevel(App)
    newWindow.title("Palabra Aceptada/Rechazada")
    anchoVentanaSmall = 150
    altoVentanaSmall = 40
    calculoPosicion = str(anchoVentanaSmall) + "x" + str(altoVentanaSmall) + "+" + str(x_ventana+350) + "+" + str(y_ventana+200)
    newWindow.geometry(calculoPosicion)  
    #newWindow. 
    if palabraValidada.get():
        ttk.Label(newWindow,text="Palabra Aceptada").pack()
    else:
        ttk.Label(newWindow,text="Palabra Rechazada").pack()
# Definir Variables para Utilizar en Transiciones:
EstadoTransicion = StringVar()
caracterTransicion = StringVar()
pilaTransicion = StringVar()

# Definir estado
estadoInicial = StringVar()

# Definir Estilos, para diferenciar frames.
estilo1 = ttk.Style()
estilo2 = ttk.Style()
estilo3 = ttk.Style()

estilo1.configure('Transiciones.TFrame', background='red',
                  relief='raised', borderwidth=5)
estilo2.configure('TransicionesTodas.TFrame', background='blue')
estilo3.configure('Estados.TFrame', background='green')

# Frame general
contenidoTransiciones = ttk.Frame(App)

# Crear los Frames generales
frameEstInicial = ttk.Frame(contenidoTransiciones)
frameTransicion = ttk.Frame(contenidoTransiciones)
frameTransicion.config(width=700, height=100)
frameTransicion.grid_propagate(0)
frameContAPD = ttk.Frame(frameTransicion)
frameTodasLasTransiciones = ttk.Frame(contenidoTransiciones)
framePalabraEstados = ttk.Frame(contenidoTransiciones)

# Definir El pocicionamiento de los Frames.
contenidoTransiciones.grid(column=0, row=0)
frameEstInicial.grid(column=0, row=0)
frameTransicion.grid(column=0, row=1, columnspan=2)
frameTodasLasTransiciones.grid(column=0, row=2)
framePalabraEstados.grid(column=1, row=2)


def getEntries():
    getEntryTransicionesEstado = entryTransicionesEstado.get()
    getEntryTransicionesCaracter = entryTransicionesCaracter.get()
    getEntryTransicionesPila = entryTranscionesPila.get()
    getEntryTransicionesEstadoSiguiente = entryTransicionesEstadoSiguiente.get()
    getEntryTransicionesAccionPila = entryTransicionesAccionPila.get()

    
    if (len(getEntryTransicionesEstado) == 0 or len(getEntryTransicionesCaracter) == 0 or len(getEntryTransicionesPila) == 0 or len(getEntryTransicionesEstadoSiguiente) == 0 or len(getEntryTransicionesAccionPila) == 0 or getEntryTransicionesEstado == "Estado" or getEntryTransicionesCaracter == "Caracter" or getEntryTransicionesPila == "Pila" or getEntryTransicionesEstadoSiguiente == "Estado" or getEntryTransicionesAccionPila == "Acción Pila"):
        pass
    else:
        listBoxTodasLasTranssiciones.insert(END, "𝜹(" + getEntryTransicionesEstado + "," + getEntryTransicionesCaracter + "," +
                                            getEntryTransicionesPila + ") = (" + getEntryTransicionesEstadoSiguiente + "," + getEntryTransicionesAccionPila + ")")
        entryTransicionesEstado.delete(0, END)
        entryTransicionesCaracter.delete(0, END)
        entryTranscionesPila.delete(0, END)
        entryTransicionesEstadoSiguiente.delete(0, END)
        entryTransicionesAccionPila.delete(0, END)

def getEntriesEstadosFinales():
    getEntryEstadosFinales = entryEstadoEstadosFinales.get()
    #listBoxTodosLosEstadoFinales.insert(END,getEntryEstadosFinales)



def obtenerTransiciones():
    size = listBoxTodasLasTranssiciones.size()
    dicTransiciones = {}
    lista = []
    lista2 = []
    for i in range(size):
        #print(f"Elemento: {i} , valor: {listBoxTodasLasTranssiciones.get(i)}")
        palabra = listBoxTodasLasTranssiciones.get(i)
        clavePalabra = palabra[0:palabra.index(")")+1]
        x = palabra.index("=")
        valorPalabra = palabra[x+2::]
        AC = ""
        for j in clavePalabra:
            if j != "(" and j != "," and j!= ")" and j!="" and j!= "𝜹":
                AC+=j
            else:
                lista.append(AC)
                AC = ""
        AC = ""
        for j in valorPalabra:
            if j != "(" and j != "," and j!= ")" and j!="" :
                AC+=j
            else:
                lista2.append(AC)
                AC = ""
        
        lista.remove("")
        lista.remove("")
        lista2.remove("")
        #print(tuple(lista),"a",tuple(lista2),"b")
        dicTransiciones[tuple(lista)] = tuple(lista2)
        lista.clear()
        lista2.clear()
        
    palabraComprobar = entryPalabra.get()
    #size = listBoxTodosLosEstadoFinales.size()
    #estadosFinales = []
    #for i in range(size):
    #    estadosFinales.append(listBoxTodosLosEstadoFinales.get(i))
    #print(dicTransiciones)
    estadosfinales = entryEstadoEstadosFinales.get()
    #print(f"Estado Final {misteriosa}''")
    if cb.get() ==1:
        #print(f'Transiciones: {dicTransiciones}.<\nEstadoFinal: {True} \nEstadoInicial {entryInitialState.get()}.< \nPalabra: {palabraComprobar+"e"}.< \nEstadosFinales {estadosfinales}.<')
        elem = validarPalabra(dicTransiciones,entryInitialState.get(), True, palabraComprobar+"e", estadosfinales)
        palabraValidada.set(elem)
        #print("INICIAL 1: " + estadoInicial)
    else:
        #print(f'Transiciones: {dicTransiciones}\n, EstadoFinal: {False}')
        elem = validarPalabra(dicTransiciones,entryInitialState.get(), False, palabraComprobar+"e")
        palabraValidada.set(elem)
        #print("INICIAL 0: " + estadoInicial)
    '''
    transiciones3 = {
                 ("q0","a","R"): ("q0","AR"),
                 ("q0","a","A"): ("q0","AA"),
                 ("q0","b","A"): ("q1","e"),
                 ("q1","b","A"): ("q1","e"),
                 ("q1","b","R"): ("q2","R"),
                 ("q2","b","R"): ("q2","R"),
                 ("q2","e","R"): ("q3","R")
                 }
    '''
    openNewWindow()

# Frame transiciones, todos los elementos que contiene.

labelEP = ttk.Label(frameContAPD, text="𝜹", font=('Arial',15))
labelPar1 = ttk.Label(frameContAPD, text="(", font=('Arial',15))
labelCom1 = ttk.Label(frameContAPD, text=",", font=('Arial',15))
labelCom2 = ttk.Label(frameContAPD, text=",", font=('Arial',15))
labelPar2 = ttk.Label(frameContAPD, text=")", font=('Arial',15))
labelPar3 = ttk.Label(frameContAPD, text="(", font=('Arial',15))
labelPar4 = ttk.Label(frameContAPD, text=")", font=('Arial',15))
labelCom3 = ttk.Label(frameContAPD, text=",", font=('Arial',15))
labelTransiciones = ttk.Label(frameContAPD, text="Transiciones")
entryTransicionesEstado = ttk.Entry(frameContAPD, width=12)
entryTransicionesCaracter = ttk.Entry(frameContAPD, width=10)
entryTranscionesPila = ttk.Entry(frameContAPD, width=10)
labelTranscionesIgual = ttk.Label(frameContAPD, text="=")
entryTransicionesEstadoSiguiente = ttk.Entry(frameContAPD, width=10)
entryTransicionesAccionPila = ttk.Entry(frameContAPD, width=10)
botonTransicionesagregar = ttk.Button(
    frameContAPD, text="Agregar", command=getEntries)


# Creacion place holders Todos los entrys Transiciones
# PlaceHolder Estado
entryTransicionesEstado.insert(0, "Estado")
entryTransicionesEstado.config(state=DISABLED)
entryTransicionesEstado.bind(
    "<Button-1>", lambda event: [entryTransicionesEstado.config(state=NORMAL), entryTransicionesEstado.delete(0, END)])

# PlaceHolder Caracter
entryTransicionesCaracter.insert(0, "Caracter")
entryTransicionesCaracter.config(state=DISABLED)
entryTransicionesCaracter.bind(
    "<Button-1>", lambda event: [entryTransicionesCaracter.config(state=NORMAL), entryTransicionesCaracter.delete(0, END)])

# PlaceHolder Transiciones pila
entryTranscionesPila.insert(0, "Pila")
entryTranscionesPila.config(state=DISABLED)
entryTranscionesPila.bind(
    "<Button-1>", lambda event: [entryTranscionesPila.config(state=NORMAL), entryTranscionesPila.delete(0, END)])

# PlaceHolder Estado siguiente
entryTransicionesEstadoSiguiente.insert(0, "Estado")
entryTransicionesEstadoSiguiente.config(state=DISABLED)
entryTransicionesEstadoSiguiente.bind(
    "<Button-1>", lambda event: [entryTransicionesEstadoSiguiente.config(state=NORMAL), entryTransicionesEstadoSiguiente.delete(0, END)])

# PlaceHolder Acción pila
entryTransicionesAccionPila.insert(0, "Acción pila")
entryTransicionesAccionPila.config(state=DISABLED)
entryTransicionesAccionPila.bind(
    "<Button-1>", lambda event: [entryTransicionesAccionPila.config(state=NORMAL), entryTransicionesAccionPila.delete(0, END)])

# Definir posicionamiento objetos Frame transiciones.
frameContAPD.grid(column=0, row=0)
frameContAPD.place(relx=0.5, rely= 0.5, anchor=CENTER)
labelTransiciones.grid(column=0, row=1, columnspan=7,sticky="")
labelEP.grid(column=0,row=2)
labelPar1.grid(column=1,row=2)
entryTransicionesEstado.grid(column=2, row=2)
labelCom1.grid(column=3,row=2)
entryTransicionesCaracter.grid(column=4, row=2)
labelCom2.grid(column=5,row=2)
entryTranscionesPila.grid(column=6, row=2)
labelPar2.grid(column=7,row=2)
labelTranscionesIgual.grid(column=8, row=2)
labelPar3.grid(column=9,row=2)
entryTransicionesEstadoSiguiente.grid(column=10, row=2)
labelCom3.grid(column=11,row=2)
entryTransicionesAccionPila.grid(column=12, row=2)
labelPar4.grid(column=13,row=2)
botonTransicionesagregar.grid(column=14, row=2)

# Crear barra de desplazamiento
scrollbar = ttk.Scrollbar(frameTodasLasTransiciones, orient=VERTICAL)

# Frame Todas las transiciones todos los elementos que contiene. A = all
labelTodasLastransiciones = ttk.Label(
    frameTodasLasTransiciones, text="APD")
listBoxTodasLasTranssiciones = Listbox(
    frameTodasLasTransiciones, height=10, yscrollcommand=scrollbar.set, font=Font(family="Saans Serif", size=10))

scrollbar.config(command=listBoxTodasLasTranssiciones.yview)
scrollbar.grid(row=1, column=2, sticky=N+S)

# Definir posicionamiento objetos Frame Todas las transiciones.
labelTodasLastransiciones.grid(column=0, row=0)
listBoxTodasLasTranssiciones.grid(column=0, row=1)


# Frame estados todos los elementos que contiene.
frameContenedorPalabra = ttk.Frame(framePalabraEstados)


FrameEstadoInicial = ttk.Frame(frameEstInicial)

labelEstadoInicial = ttk.Label(
    FrameEstadoInicial, text="Estado Inicial")

entryInitialState = StringVar()


def isInStateEmpty(var, index, mode):
    if(len(entryInitialState.get()) != 0):
        botonEstadoInicial.config(state=NORMAL)
    else:
        botonEstadoInicial.config(state=DISABLED)


entryInitialState.trace_add('write', isInStateEmpty)

entryEstadoInicial = ttk.Entry(
    FrameEstadoInicial, width=7, textvariable=entryInitialState)

def addInitialState():
    entryEstadoInicial.config(state=DISABLED)
    botonEstadoInicial.config(state=DISABLED)

entryEstadoInicial.config(state=NORMAL)

botonEstadoInicial = ttk.Button(FrameEstadoInicial, text="Agregar", command=addInitialState)
botonEstadoInicial.config(state=DISABLED)
frameEstadosFinales = ttk.Frame(framePalabraEstados)

cb = IntVar()

def isSelected():
    if(cb.get() == 1):
        entryEstadoEstadosFinales.config(state=NORMAL)
        if(len(entryStateFinal.get()) != 0):
            botonAgregarEstadosFinales.config(state=NORMAL)
    elif(cb.get() == 0):
        entryEstadoEstadosFinales.config(state=DISABLED)
        botonAgregarEstadosFinales.config(state=DISABLED)


checkEstadoFinal = ttk.Checkbutton(
    frameEstadosFinales, text="Estado Final", variable=cb, onvalue=1, offvalue=0, command=isSelected)
labelEstadosFinales = ttk.Label(frameEstadosFinales, text="Estado Final")

entryStateFinal = StringVar()


def isStateEmpty(var, index, mode):
    if(len(entryStateFinal.get()) != 0 and cb.get() == 1):
        botonAgregarEstadosFinales.config(state=NORMAL)
    else:
        botonAgregarEstadosFinales.config(state=DISABLED)


entryStateFinal.trace_add('write', isStateEmpty)

def addFinalState():
    entryEstadoEstadosFinales.config(state=DISABLED)
    botonAgregarEstadosFinales.config(state=DISABLED)

entryEstadoEstadosFinales = ttk.Entry(
    frameEstadosFinales, width=7, textvariable=entryStateFinal)
entryEstadoEstadosFinales.config(state=DISABLED)
botonAgregarEstadosFinales = ttk.Button(frameEstadosFinales, text="Agregar",command=addFinalState)
botonAgregarEstadosFinales.config(state=DISABLED)

#frameTodosLosEstadosFinales = ttk.Frame(framePalabraEstados)
#LPestadosFinales = ttk.Label(
#    frameTodosLosEstadosFinales, text="Todos los estados finales")
#listBoxTodosLosEstadoFinales = Listbox(frameTodosLosEstadosFinales)


# Comprobar Palabra

palabra = StringVar()


def isWordEmpty(var, index, mode):
    if(len(palabra.get()) != 0):
        comprobarPalabra.config(state=NORMAL)
    else:
        comprobarPalabra.config(state=DISABLED)


palabra.trace_add('write', isWordEmpty)
framePalabra = ttk.Frame(contenidoTransiciones)
labelPalabra = ttk.Label(framePalabra, text="Palabra")
entryPalabra = ttk.Entry(framePalabra, width=15, textvariable=palabra)
comprobarPalabra = ttk.Button(
    framePalabra, text="Comprobar Palabra", command=obtenerTransiciones)
comprobarPalabra.config(state=DISABLED)
labelCompPalabra = ttk.Label(contenidoTransiciones, text="e = Epsilon", font='Helvetica 10 bold')

# Posicionamiento comprobar palabra
framePalabra.grid(column=0, row=4, columnspan=2)
labelPalabra.grid(column=0, row=0)
entryPalabra.grid(column=1, row=0)
comprobarPalabra.grid(column=2, row=0)
labelCompPalabra.grid(column=0, row=5, columnspan=2, sticky="ES")

# Definir posicionamiento objetos Frame Estados.
frameContenedorPalabra.grid(column=0, row=1)
#frameTodosLosEstadosFinales.grid(column=1, row=2)

FrameEstadoInicial.grid(column=0, row=0)
labelEstadoInicial.grid(column=0, row=0)

entryEstadoInicial.grid(column=0, row=1)
botonEstadoInicial.grid(column=1, row=1)

frameEstadosFinales.grid(column=0, row=2)

checkEstadoFinal.grid(column=0, row=0)
labelEstadosFinales.grid(column=0, row=1)
entryEstadoEstadosFinales.grid(column=0, row=2)
botonAgregarEstadosFinales.grid(column=1, row=2)

#LPestadosFinales.grid(column=1, row=2)
#listBoxTodosLosEstadoFinales.grid(column=1, row=3)

contenidoTransiciones.place(relx=0.5, rely=0.5, anchor=CENTER)


# Ejecutar en bucle
App.mainloop()
