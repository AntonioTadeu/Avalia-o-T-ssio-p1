from flask import Flask 
import os
from application.model.entity.noticia import Noticia
from application.model.entity.categoria import Categoria


template_folder = os.path.abspath("application/view/templates")
static_folder = os.path.abspath("application/view/static")

app = Flask(__name__, template_folder = template_folder, static_folder = static_folder)

noticia1 = Noticia(1, "Covid-19: cidade no Rio de Janeiro fecha comércio não essencial", "Nova Friburgo, na região serrana do estado do Rio de Janeiro, voltou a determinar o fechamento do comércio não essencial. A decisão foi tomada na última sexta-feira (17) e passa a valer a partir de hoje (20), A prefeitura tomou a decisão de voltar à bandeira vermelha depois de perceber que a ocupação de leitos de terapia intensiva (UTI) chegou a 75 porcento da capacidade para atendimento a pacientes com covid-19. De acordo com decreto municipal de 1º de julho, o processo de reabertura do comércio de Nova Friburgo prevê, de acordo com avaliações semanais da situação dos leitos de UTI, que a bandeira vermelha (a mais restritiva) seja aplicada quando a ocupação desses leitos superar 70%.", "video/rio_novo2.mp4", "img/rio de janeiroo.png")
noticia2 = Noticia(2, "São Paulo tem queda no numero de mortes pela terceira semana consecutiva ", "São Paulo chegou à terceira semana seguida com queda no número de mortes por covid-19. De acordo com dados divulgados hoje pelo governo paulista, o estado teve 1.706 vítimas fatais da doença causada pelo novo coronavírus na última semana, 27 a menos do que na anterior. Os dados apresentados mostram que a capital teve redução de quase 6 porcento, enquanto a Região Metropolitana teve uma redução de 14,5 porcento no número de mortes. O interior, no entanto, teve crescimento de 12 porcento. São Paulo está na 29ª semana epidemiológica da pandemia - cada semana no domingo e vai até sábado", "video/sao paulo.mp4", "img/sao paulo.png")
noticia3 = Noticia(3, "Minas Gerais tem a maior ocupação de leitos do país", "A situação da pandemia em Minas Gerais continua crítica. O estado tem a maior ocupação de leitos do país e a Polícia Militar vai ajudar a orientar a população. Especialistas dizem que o aumento de casos está relacionado ao número de testes. Sem examinar a população para isolar e tratar os infectados, o vírus se espalha muito mais rápido. E Minas é o segundo estado do país que menos faz testes para diagnosticar o coronavírus.", "video/Minas_novo.mp4", "img/minas gerais.png")
todas_noticias = [noticia1, noticia2, noticia3]

todas_categorias = []
todas_categorias.append(Categoria(1, "Rio de Janeiro", [noticia1]))
todas_categorias.append(Categoria(2, "São Paulo", [noticia2]))
todas_categorias.append(Categoria(3, "Minas Gerais", [noticia3]))


from application.controller import home_controller
from application.controller import categoria_controller
from application.controller import noticia_controller