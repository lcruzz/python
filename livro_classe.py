class livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
    def detalhes(self):
        print("O livro", self.titulo, "foi publicado pelo autor(a)", self.autor, "no ano de", self.ano_publicado)

livraria = livro(autor = input("Informe o nome do autor: "), titulo = input("Informe o nome do livro: "), ano_publicado = int(input("Informe o ano de publicação do livro: ")))
livraria.detalhes()
