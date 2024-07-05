from django.urls import path
from . import views


urlpatterns = [
    path('pesquisar',views.pesquisar, name='pesquisar'),
    path('cadastrar',views.cadastrar, name='cadastrar'),
    path('deletar',views.deletar, name='deletar'),
    path('atualizar',views.atualizar, name='atualizar'),

]