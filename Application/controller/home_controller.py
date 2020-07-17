from application import app
from application import todas_noticias
from application import todas_categorias
from flask import render_template, request
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.noticia import Noticia


@app.route("/")
def home():
    categoriadao = CategoriaDAO()
    lista_de_categoria = categoriadao.retornar_todas_noticias()
    
    lista_mais_curtidos_ordem = sorted(todas_noticias, key=Noticia.get_total_curtidas, reverse=True)
    lista_mais_curtidos = [lista_mais_curtidos_ordem[0], lista_mais_curtidos_ordem[1]]

    return render_template("index.html", lista_de_categoria = lista_de_categoria, lista_mais_curtidos = lista_mais_curtidos)