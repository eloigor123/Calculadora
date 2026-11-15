from tkinter import *

janela = Tk()
janela.title("Calculadora")

visor = Entry(janela, font=("Arial", 16), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

primeiro_numero = 0
operacao = ""

def clique(tecla):
    if tecla == "." and "." in visor.get():
        return
    visor.insert(END, str(tecla))

def definir_operacao(op):
    global primeiro_numero, operacao
    if visor.get() != "":
        primeiro_numero = float(visor.get())
        operacao = op
        visor.delete(0, END)

def calcular():
    global primeiro_numero, operacao
    if visor.get() == "" or operacao == "":
        return
    
    segundo_numero = float(visor.get())
    resultado = 0
    
    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero
    elif operacao == "×":
        resultado = primeiro_numero * segundo_numero
    elif operacao == "÷":
        if segundo_numero == 0:
            visor.delete(0, END)
            visor.insert(0, "Erro: divisão por zero")
            return
        resultado = primeiro_numero / segundo_numero
        
    visor.delete(0, END)
    visor.insert(0, str(resultado))
    operacao = ""

def limpar():
    global primeiro_numero, operacao
    primeiro_numero = 0
    operacao = ""
    visor.delete(0, END)

def apagar():
    texto = visor.get()
    if len(texto) > 0:
        visor.delete(len(texto)-1, END)

btn_c = Button(janela, text="C", width=5, command=limpar)
btn_c.grid(row=1, column=0, padx=2, pady=2)

btn_apagar = Button(janela, text="⌫", width=5, command=apagar)
btn_apagar.grid(row=1, column=1, padx=2, pady=2)

btn_div = Button(janela, text="÷", width=5, command=lambda: definir_operacao("÷"))
btn_div.grid(row=1, column=2, padx=2, pady=2)

btn_mult = Button(janela, text="×", width=5, command=lambda: definir_operacao("×"))
btn_mult.grid(row=1, column=3, padx=2, pady=2)


btn_7 = Button(janela, text="7", width=5, command=lambda: clique(7))
btn_7.grid(row=2, column=0, padx=2, pady=2)

btn_8 = Button(janela, text="8", width=5, command=lambda: clique(8))
btn_8.grid(row=2, column=1, padx=2, pady=2)

btn_9 = Button(janela, text="9", width=5, command=lambda: clique(9))
btn_9.grid(row=2, column=2, padx=2, pady=2)

btn_menos = Button(janela, text="-", width=5, command=lambda: definir_operacao("-"))
btn_menos.grid(row=2, column=3, padx=2, pady=2)


btn_4 = Button(janela, text="4", width=5, command=lambda: clique(4))
btn_4.grid(row=3, column=0, padx=2, pady=2)

btn_5 = Button(janela, text="5", width=5, command=lambda: clique(5))
btn_5.grid(row=3, column=1, padx=2, pady=2)

btn_6 = Button(janela, text="6", width=5, command=lambda: clique(6))
btn_6.grid(row=3, column=2, padx=2, pady=2)

btn_mais = Button(janela, text="+", width=5, command=lambda: definir_operacao("+"))
btn_mais.grid(row=3, column=3, padx=2, pady=2)


btn_1 = Button(janela, text="1", width=5, command=lambda: clique(1))
btn_1.grid(row=4, column=0, padx=2, pady=2)

btn_2 = Button(janela, text="2", width=5, command=lambda: clique(2))
btn_2.grid(row=4, column=1, padx=2, pady=2)

btn_3 = Button(janela, text="3", width=5, command=lambda: clique(3))
btn_3.grid(row=4, column=2, padx=2, pady=2)

btn_igual = Button(janela, text="=", width=5, height=3, command=calcular)
btn_igual.grid(row=4, column=3, rowspan=2, padx=2, pady=2)


btn_0 = Button(janela, text="0", width=12, command=lambda: clique(0))
btn_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

btn_ponto = Button(janela, text=".", width=5, command=lambda: clique("."))
btn_ponto.grid(row=5, column=2, padx=2, pady=2)

janela.mainloop()