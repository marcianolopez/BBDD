from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
#---------------------------------FUNCIONES-----------------------------------------------

def conexionBBDD():
    
    miConexion=sqlite3.connect('Usuarios')

    micursor=miConexion.cursor()

    try:    
        
        micursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(10),
            PASSWORD VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')

        messagebox.showinfo('BBDD', 'BBDD creada con exito')

    except:
        
        messagebox.showwarning('Atencion', 'La BBDD ya existe')

def salirAplicacion():
    
    valor=messagebox.askquestion('Salir', 'Desea salir de la aplicacion?')

    if valor=='yes':
        root.destroy()


def limpiarCampos():

    miNombre.set('')
    miId.set('')
    miApellido.set('')
    miDireccion.set('')
    miPass.set('')
    textocomentario.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect('Usuarios')

    micursor=miConexion.cursor()

    datos=miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), textocomentario.get('1.0', END)

    """micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() + 
    "','" + miApellido.get() +
    "','" + miPass.get() +
    "','" + miDireccion.get() +
    "','" + textocomentario.get('1.0', END) + "')")"""

    micursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

    miConexion.commit()

    messagebox.showinfo('BBDD', 'Registro creado con exito')


def leer():
    
    miConexion=sqlite3.connect('Usuarios')

    micursor=miConexion.cursor() 

    micursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario=micursor.fetchall()

    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        textocomentario.insert(1.0, usuario[5])
    
    miConexion.commit()


def actualizar():
    
    miConexion=sqlite3.connect('Usuarios')

    micursor=miConexion.cursor()
    datos=miNombre.get(), miApellido.get(), miPass.get(), miDireccion.get(), textocomentario.get('1.0', END)

    """micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + 
    "', APELLIDO='" + miApellido.get() +
    "', PASSWORD='" + miPass.get() +
    "', DIRECCION='" + miDireccion.get() +
    "', COMENTARIOS='" + textocomentario.get("1.0", END) +
    "' WHERE ID=" + miId.get())"""

    micursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=? " + 
    "WHERE ID=" + miId.get(), (datos))
    miConexion.commit()

    messagebox.showinfo('BBDD', 'Registro actualizado con exito')   

def borrar():

    miConexion=sqlite3.connect('Usuarios')

    micursor=miConexion.cursor()

    micursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con exito")


def acercade():

    messagebox.showinfo("Ayuda", "Aplicacion creada por Mariano Lopez")

def licencia():

    messagebox.showinfo('Ayuda', 'Licencia Creative Commons')

 
#----------------------------Barra Menus--------------------------------------------------
        
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='Conectar', command=conexionBBDD)
bbddMenu.add_command(label='Salir', command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label='Borrar campos', command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label='Crear', command=crear)
crudMenu.add_command(label='Leer', command=leer)
crudMenu.add_command(label='Actulizar', command=actualizar)
crudMenu.add_command(label='Borrar', command=borrar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label='Licencia', command=licencia)
ayudaMenu.add_command(label='Acerca de...', command=acercade)

barraMenu.add_cascade(label='BBDD', menu=bbddMenu)
barraMenu.add_cascade(label='Borrar', menu=borrarMenu)
barraMenu.add_cascade(label='CRUD', menu=crudMenu)
barraMenu.add_cascade(label='Ayuda', menu=ayudaMenu)

#-------------------------------comienzo de campos------------------------------------------

miframe=Frame(root)
miframe.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miframe, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miframe, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido=Entry(miframe, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass=Entry(miframe, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show='*')

cuadroDireccion=Entry(miframe, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textocomentario=Text(miframe, width=22, height=5)
textocomentario.grid(row=5, column=1, pady=10, padx=10)
scrollvert=Scrollbar(miframe, command=textocomentario.yview)
scrollvert.grid(row=5, column=2, sticky='nsew')

textocomentario.config(yscrollcommand=scrollvert.set)

#-------------------------LABELS---------------------------------------------------

idLabel=Label(miframe, text='Id:')
idLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

nombreLabel=Label(miframe, text='Nombre')
nombreLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

apellidoLabel=Label(miframe, text='Apellido')
apellidoLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

passLabel=Label(miframe, text='Password')
passLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)


direccionLabel=Label(miframe, text='Direccion')
direccionLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

commentLabel=Label(miframe, text='Comentarios')
commentLabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

#------------------------------BOTONES-------------------------------------------------

miframe2=Frame(root)
miframe2.pack()

botonCrear=Button(miframe2, text='Create', command=crear)
botonCrear.grid(row=0, column=0, sticky='e', pady=10, padx=10)

botonLeer=Button(miframe2, text='Read', command=leer)
botonLeer.grid(row=0, column=1, sticky='e', pady=10, padx=10)

botonActualizar=Button(miframe2, text='Update', command=actualizar)
botonActualizar.grid(row=0, column=2, sticky='e', pady=10, padx=10)

botonBorrar=Button(miframe2, text='Delete', command=borrar)
botonBorrar.grid(row=0, column=3, sticky='e', pady=10, padx=10)

root.mainloop()