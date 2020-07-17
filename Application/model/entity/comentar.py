class Comentar:
    def __init__(self, conteudo, nome):
        self._conteudo = conteudo
        self._nome = nome

    def get_conteudo(self):
        return self._conteudo

    def get_nome(self):
        return self._nome