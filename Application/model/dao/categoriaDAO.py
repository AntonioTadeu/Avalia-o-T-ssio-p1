from application.model.entity.categoria import Categoria
from application.model.entity.noticia import Noticia
from application import todas_categorias

class CategoriaDAO:
    def __init__(self):
        self.todas_categorias = todas_categorias

    def retornar_lista_categorias(self):
        return todas_categorias

    def procurar(self, id):
        for i in range(0, len(todas_categorias)):
            if todas_categorias[i].get_id() == int(id):
                return todas_categorias[i] 
        return None