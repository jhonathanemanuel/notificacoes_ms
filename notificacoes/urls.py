from django.urls import path
from . import views

app_name = 'notificacoes'

urlpatterns = [
    # Rota 1: Retorna a contagem de não lidas
    path('api/notificacoes/nao-lidas/', views.NotificacoesNaoLidasCountView.as_view(), name='contagem-nao-lidas'),

    # Rota 2: Lista todas as notificações do usuário
    path('api/notificacoes/', views.NotificacoesListView.as_view(), name='lista-notificacoes'),

    # Rota 3: Marca uma notificação específica como lida (espera o ID na URL)
    path('api/notificacoes/<int:pk>/lida/', views.NotificacaoMarcarLidaView.as_view(), name='marcar-lida'),
]