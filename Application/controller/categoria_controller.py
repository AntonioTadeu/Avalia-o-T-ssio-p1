from application import app
from flask import render_template, request
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.entity.categoria import Categoria


@app.route("/categorias/<categoria_id>")
def category(categoria_id):
    categoria = CategoriaDAO().procurar(categoria_id)
    categoriadao = CategoriaDAO()
    categoria_lista = categoriadao.retornar_lista_categorias()
    return render_template("opcao-de-categoria-selecionada.html", categoria = categoria, categoria_lista = categoria_lista)