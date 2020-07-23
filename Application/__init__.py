from flask import Flask 
import os
from application.model.entity.noticia import Noticia
from application.model.entity.categoria import Categoria


template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)

noticia1 = Noticia(1, "Covid-19: cidade no Rio de Janeiro fecha comércio não essencial", "Nova Friburgo, na região serrana do estado do Rio de Janeiro, voltou a determinar o fechamento do comércio não essencial. A decisão foi tomada na última sexta-feira (17) e passa a valer a partir de hoje (20), A prefeitura tomou a decisão de voltar à bandeira vermelha depois de perceber que a ocupação de leitos de terapia intensiva (UTI) chegou a 75 porcento da capacidade para atendimento a pacientes com covid-19. De acordo com decreto municipal de 1º de julho, o processo de reabertura do comércio de Nova Friburgo prevê, de acordo com avaliações semanais da situação dos leitos de UTI, que a bandeira vermelha (a mais restritiva) seja aplicada quando a ocupação desses leitos superar 70%.", "video/rio_novo2.mp4", "img/rio de janeiroo.png")
noticia2 = Noticia(2, "Governo de São Paulo atinge marca de 3 mil respiradores distribuídos", "Descrição da notícia 2", "video/sao paulo.mp4", "img/sao paulo.png")
noticia3 = Noticia(3, "Titulo da terceira notícia", "Descrição da notícia 3", "video/diretoriodabandeira", "img/minas gerais.png")
todas_noticias = [noticia1, noticia2, noticia3]

todas_categorias = []
todas_categorias.append(Categoria(1, "Rio de Janeiro", [noticia1]))
todas_categorias.append(Categoria(2, "São Paulo", [noticia2]))
todas_categorias.append(Categoria(3, "Minas Gerais", [noticia3]))


from application.controller import home_controller
from application.controller import categoria_controller
from application.controller import noticia_controller