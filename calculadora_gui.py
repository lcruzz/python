import tkinter as tk
import math

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("1500x400")
janela.config(bg="#191970")

fonte = ("Times New Roman", 13)

def adicao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 + num2

    rotulo_result.config(text=resultado)
    print(resultado)
    
def subtracao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 - num2

    rotulo_result.config(text=resultado)
    print(resultado)
    
def multiplicacao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1 * num2

    rotulo_result.config(text=resultado)
    print(resultado)
    
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
        print(resultado)
    
def potenciacao():
    num1 = float(numero1.get())
    num2 = float(numero2.get())
    resultado = num1**num2

    rotulo_result.config(text=resultado)
    print(resultado)
    
def radiciacao():
    num1 = float(numero1.get())
    resultado = math.sqrt(num1)

    rotulo_result.config(text=resultado)
    print(resultado)

def aleatorio():
    import random
    resultado = random.randint(1, 100)

    rotulo_sort.config(text=resultado)
    print(resultado)

rotulo_num1 = tk.Label(janela, text="Informe o primeiro número:", bg="#191970", font=fonte, fg="white")
rotulo_num1.pack(padx=5, pady=5)

numero1 = tk.Entry(width=10)
numero1.pack(padx=5)

rotulo_num2 = tk.Label(janela, text="Informe o segundo número:", bg="#191970", font=fonte, fg="white")
rotulo_num2.pack(padx=5, pady=5)

numero2 = tk.Entry(width=10)
numero2.pack(padx=5)

rotulo_result = tk.Label(janela, text="O resultado aparecerá aqui", font=fonte, bg="#191970", fg="white")
rotulo_result.pack(padx=10, pady=10)

rotulo_sort = tk.Label(janela, text="Um número aleatório aparecerá aqui", font=fonte, bg="#191970", fg="white")
rotulo_sort.pack(padx=10, pady=10)

soma = tk.Button(janela, text="+", width=5, bg="#4F94CD", fg="#191970", command=adicao)
soma.place(x=400, y=20)

sub = tk.Button(janela, text="-", width=5, bg="#4F94CD", fg="#191970", command=subtracao)
sub.place(x=450, y=20)

multi = tk.Button(janela, text="x", width=5, bg="#4F94CD", fg="#191970", command=multiplicacao)
multi.place(x=500, y=20)

div = tk.Button(janela, text="÷", width=5, bg="#4F94CD", fg="#191970", command=divisao)
div.place(x=500, y=50)

potencia = tk.Button(janela, text="^", width=5, bg="#4F94CD", fg="#191970", command=potenciacao)
potencia.place(x=450, y=50)

raiz = tk.Button(janela, text="√", width=5, bg="#4F94CD", fg="#191970", command=radiciacao)
raiz.place(x=400, y=50)

numeros_gerados = tk.Button(janela, text="sortear número", width=15, bg="#4F94CD", fg="#191970", command=aleatorio)
numeros_gerados.place(x=414, y=80)

janela.mainloop()