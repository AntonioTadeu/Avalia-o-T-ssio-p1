from application import app
from flask import render_template, request
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.dao.noticiaDAO import NoticiaDAO
from application.model.entity.categoria import Categoria
from application.model.entity.noticia import Noticia
from application.model.entity.comentar import Comentar


@app.route("/categorias/<categoria_id>/<noticia_id>")
def exibicao(categoria_id, noticia_id):
    mostrar = CategoriaDAO().procurar(categoria_id)
    noticia = NoticiaDAO().procurar_noticia(noticia_id)
    categoria = CategoriaDAO().procurar(categoria_id)
    categoriadao = CategoriaDAO()
    noticiadao = NoticiaDAO()
    exibir_lista_noticia = noticiadao.retornar_todas_noticias()
    noticiadao.contar_visualizacao(noticia)
    return render_template("noticia.html", mostrar = mostrar, noticia = noticia, categoria = categoria, exibir_lista_noticia = exibir_lista_noticia)


@app.route("/<noticia_id>/comentario", methods=['POST'])
def coment(noticia_id):
    noticiadao = NoticiaDAO()
    noticia = noticiadao.procurar_noticia(int(noticia_id))
    autor = request.values.get('nome')
    comentario = request.values.get('comentario')
    comentar = Comentar(comentario, autor)
    noticia.set_comentario(coment)
    lista_comentario = noticia.get_comentario()
    return render_template("coment.html", noticia = noticia, lista_comentario = lista_comentario)


@app.route("/<noticia_id>/like", methods=['POST'])
def like(noticia_id):
    noticiadao = NoticiaDAO()
    noticia = noticiadao.procurar_noticia(int(noticia_id))
    noticiadao.contar_curtida(noticia)
    return render_template("like.html", noticia = noticia)