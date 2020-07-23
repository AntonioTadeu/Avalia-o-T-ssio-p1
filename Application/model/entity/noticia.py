class Noticia:
    def __init__(self, id, titulo, descricao, video, imagem_bandeira):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._video = video
        self._total_visualizacoes = 0
        self._total_curtidas = 0
        self._imagem_bandeira = imagem_bandeira
        self._comentarios = []

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def set_curtida(self, curtida):
        self._total_curtidas = curtida
        
    def get_total_curtidas(self):
        return self._total_curtidas

    def set_visualizacoes(self, visualizacoes):
        self._total_visualizacoes = visualizacoes

    def get_total_visualizacoes(self):
        return self._total_visualizacoes

    def get_video(self):
        return self._video

    def get_id(self):
        return self._id

    def set_comentario(self, comentario):
        self._comentarios.append(comentario)

    def get_comentario(self):
        return self._comentarios

    def get_imagem_bandeira(self):
        return self._imagem_bandeira