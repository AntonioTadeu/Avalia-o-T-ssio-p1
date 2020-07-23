class Comentar:
    def __init__(self, nome, conteudo):
        self._nome = nome
        self._conteudo = conteudo

    def get_nome(self):
        return self._nome

    def get_conteudo(self):
        return self._conteudo