from application import app
from application import todas_noticias
from flask import render_template, request
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.noticia import Noticia


@app.route("/")
def home():
    categoriadao = CategoriaDAO()
    lista_de_categoria = categoriadao.retornar_todas_categorias()
    
    
    lista_em_ordem_mais_curtidas = sorted(todas_noticias, key=Noticia.get_total_curtidas, reverse=True)
    noticias_mais_curtidas = [lista_em_ordem_mais_curtidas[0], lista_em_ordem_mais_curtidas[1]]

    return render_template("index.html", lista_de_categoria = lista_de_categoria, noticias_mais_curtidas = noticias_mais_curtidas)