from django.contrib import admin
from django.urls import path, include  # Garanta que o 'include' está importado aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Encaminha qualquer requisição vazia ou correspondente para o app de notificações
    path('', include('notificacoes.urls')),
]