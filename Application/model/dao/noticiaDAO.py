from application import todas_noticias
from application.model.entity.noticia import Noticia

class NoticiaDAO:
    def __init__(self):
        self._todas_noticias = todas_noticias

    def contar_visualizacao(self, noticia):
        visu = noticia.get_total_visualizacoes()
        visu += 1
        noticia.set_visualizacoes(visu)

    def retornar_todas_noticias(self):
        return self._todas_noticias

    def somar_curtida(self, noticia):
        like = noticia.get_total_curtidas()
        like += 1
        noticia.set_curtida(like)

    def procurar_noticia(self, id):
        for i in range(0, len(self._todas_noticias)):
            if self._todas_noticias[i].get_id() == int(id):
                return self._todas_noticias[i]
        return None