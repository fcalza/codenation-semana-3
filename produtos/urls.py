from django.urls import path
from produtos import views


urlpatterns = [
    path('listar', views.list_produtos),
    path('criar', views.criar_produtos),
    path('atualizar/<int:produto_id>', views.atualiza_produto)
]
