from flask import Flask 
import os
from application.model.entity.categoria import Categoria
from application.model.entity.noticia import Noticia

template_folder=os.path.abspath("application/view/templates")
static_folder=os.path.abspath("application/view/static")

app = Flask(__name__,static_folder=os.path.abspath,template_folder=os.path.abspath)

noticia1 = Noticia(1, "Titulo da primeira notícia", "Descrição da notícia 1", "img/diretoriodabandeira", "Estado1")
noticia2 = Noticia(1, "Titulo da segunda notícia", "Descrição da notícia 2", "img/diretoriodabandeira", "Estado2")
noticia3 = Noticia(1, "Titulo da terceira notícia", "Descrição da notícia 3", "img/diretoriodabandeira", "Estado3")
todas_noticias = [noticia1, noticia2, noticia3]

todas_categorias = []
todas_categorias.append(Categoria(1, "Titulo da categoria 1", [noticia1]))
todas_categorias.append(Categoria(2, "Titulo da categoria 2", [noticia2]))
todas_categorias.append(Categoria(3, "Titulo da categoria 3", [noticia3]))