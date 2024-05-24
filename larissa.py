import tkinter as tk

janela = tk.Tk()
janela.title("Larissa diva")
janela.geometry("400x400")

fonte = ("Arial", 13)

rotulo = tk.Label(janela, text="TERMINOU!!!!!! XD XD", font=fonte)
rotulo.pack(padx=10, pady=10)

def clicar():
    rotulo.config(text="#WeLoveYouLarissa")

botao = tk.Button(janela, text="Clique aqui", width=20, font=fonte, bg="#6B8E23", fg="white", command=clicar)
botao.pack(padx=10, pady=10)

janela.mainloop()