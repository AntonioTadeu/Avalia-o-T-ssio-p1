class Categoria:
    def __init__(self, id, titulo, todas_imagens):
        self._id = id
        self._titulo = titulo
        self._todas_imagens = todas_imagens

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_titulo(self):
        return self._titulo

    def get_todas_imagens(self):
        return self._todas_imagens