import tkinter as tk
import customtkinter

# Crear la ventana principal
root = customtkinter.CTk()
root.title("Calculadora")
root.geometry("640x480")



root.columnconfigure(0,weight=1, uniform="col")
root.columnconfigure(1,weight=1, uniform="col")
root.columnconfigure(2,weight=1, uniform="col")
root.columnconfigure(3,weight=1, uniform="col")


root.rowconfigure(0,weight=1,uniform="row")
root.rowconfigure(1,weight=1,uniform="row")
root.rowconfigure(2,weight=1,uniform="row")
root.rowconfigure(3,weight=1,uniform="row")
root.rowconfigure(4,weight=1,uniform="row")
root.rowconfigure(5,weight=1,uniform="row")






resultado = tk.Label(text="Resultado",bg="#bbee66")
#resultado.place()
resultado.grid(row=0, column=0, columnspan=4, sticky="nsew")

botonAC = customtkinter.CTkButton(root,text="AC",border_color="#282727",border_width=1,fg_color="#fb8b24",hover_color="#e36414",text_color="black")
botonPorcentaje = customtkinter.CTkButton(root,text="%",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#ff4081",text_color="black"   )
botonDividir = customtkinter.CTkButton(root,text="/",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#ff4081",text_color="black")
botonMultiplicar = customtkinter.CTkButton(root,text="*",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#ff4081",text_color="black")

boton7= customtkinter.CTkButton(root,text="7",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton8= customtkinter.CTkButton(root,text="8",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton9= customtkinter.CTkButton(root,text="9",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
botonRestar = customtkinter.CTkButton(root,text="-",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#7dcbce",text_color="black")


boton4= customtkinter.CTkButton(root,text="4",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton5= customtkinter.CTkButton(root,text="5",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton6= customtkinter.CTkButton(root,text="6",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
botonSumar = customtkinter.CTkButton(root,text="+",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#7dcbce",text_color="black")


boton1= customtkinter.CTkButton(root,text="1",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton2= customtkinter.CTkButton(root,text="2",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
boton3= customtkinter.CTkButton(root,text="3",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
botonIgual = customtkinter.CTkButton(root,text="=",border_color="#282727",border_width=1,fg_color="#b7c5ff",hover_color="#7dcbce",text_color="black")

botonPunto = customtkinter.CTkButton(root,text=".",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")
botonCero = customtkinter.CTkButton(root,text="0",border_color="#282727",border_width=1,fg_color="#a8dadc",hover_color="#7dcbce",text_color="black")

botonAC.grid(row=1,column=0,sticky="nsew",padx=3,pady=5)
botonPorcentaje.grid(row=1,column=1,sticky="nsew",padx=3,pady=5)
botonDividir.grid(row=1,column=2,sticky="nsew",padx=3,pady=5)
botonMultiplicar.grid(row="1",column=3,sticky="nsew",padx=3,pady=5)

boton7.grid(row=2,column=0,sticky="nsew",padx=3,pady=5)
boton8.grid(row=2,column=1,sticky="nsew",padx=3,pady=5)
boton9.grid(row=2,column=2,sticky="nsew",padx=3,pady=5)
botonRestar.grid(row=2,column=3,sticky="nsew",padx=3,pady=5)

boton4.grid(row=3,column=0,sticky="nsew",padx=3,pady=5)
boton5.grid(row=3,column=1,sticky="nsew",padx=3,pady=5)
boton6.grid(row=3,column=2,sticky="nsew",padx=3,pady=5)
botonSumar.grid(row=3,column=3,sticky="nsew",padx=3,pady=5)

boton1.grid(row=4,column=0,sticky="nsew",padx=3,pady=5)
boton2.grid(row=4,column=1,sticky="nsew",padx=3,pady=5) 
boton3.grid(row=4,column=2,sticky="nsew",padx=3,pady=5)
botonIgual.grid(row=4,column=3,sticky="nsew",padx=3,pady=5)

botonPunto.grid(row=5,column=0,sticky="nsew",padx=3,pady=5)
botonCero.grid(row=5,column=1,sticky="nsew",padx=3,pady=5)





root.mainloop()