#Laura de Souza Cruz 2º informática

import tkinter as tk
import math

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("1350x400")
janela.config(bg="#CD96CD")

fonte = ("Arial", 13)

def somar():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 + num2

    rotulo_result.config(text=resultado)
    print("O resultado da soma é", resultado)
    
def subtracao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 - num2

    rotulo_result.config(text=resultado)
    print("O resultado da subtração é", resultado)
    
def multiplicacao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 * num2

    rotulo_result.config(text=resultado)
    print("O resultado da multiplicação é", resultado)
    
def divisao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    if num2 == 0:
        resultado = "Erro: Impossível dividir por 0."
        rotulo_result.config(text=resultado)
        print(resultado)
    else:
        resultado = num1 / num2
        rotulo_result.config(text=resultado)
        print("O resultado da divisão é", resultado)
    
def potenciacao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1**num2

    rotulo_result.config(text=resultado)
    print("O resultado da potenciação é", resultado)
    
def radiciacao():
    num1 = float(numero1.get())
    resultado = math.sqrt(num1)

    rotulo_result.config(text=resultado)
    print("O resultado da raiz é", resultado)

def aleatorio():
    import random
    resultado = random.randint(1, 100)

    rotulo_result.config(text=resultado)
    print("O número gerado é", resultado)

rotulo_num1 = tk.Label(janela, text="Informe o primeiro número:", bg="#CD96CD", font=fonte)
rotulo_num1.pack(padx=5, pady=5)

numero1 = tk.Entry(width=10)
numero1.pack(padx=5)

rotulo_num2 = tk.Label(janela, text="Informe o segundo número:", bg="#CD96CD", font=fonte)
rotulo_num2.pack(padx=5, pady=5)

numero2 = tk.Entry(width=10)
numero2.pack(padx=5)

rotulo_result = tk.Label(janela, text="", font=fonte, bg="#CD96CD")
rotulo_result.pack(padx=10, pady=10)

soma = tk.Button(janela, text="+", width=5, bg="#8B008B", fg="white", command=somar)
soma.place(x=450, y=20)

subtrai = tk.Button(janela, text="-", width=5, bg="#8B008B", fg="white", command=subtracao)
subtrai.place(x=450, y=50)

multi = tk.Button(janela, text="x", width=5, bg="#8B008B", fg="white", command=multiplicacao)
multi.place(x=450, y=80)

divide = tk.Button(janela, text="÷", width=5, bg="#8B008B", fg="white", command=divisao)
divide.place(x=500, y=20)

potencia = tk.Button(janela, text="^", width=5, bg="#8B008B", fg="white", command=potenciacao)
potencia.place(x=500, y=50)

raiz = tk.Button(janela, text="√", width=5, bg="#8B008B", fg="white", command=radiciacao)
raiz.place(x=500, y=80)

num_gerados = tk.Button(janela, text="sortear número", width=15, bg="#8B008B", fg="white", command=aleatorio)
num_gerados.place(x=440, y=110)

janela.mainloop()