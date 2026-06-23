from django.contrib import admin
from .models import Empresa, Target, Notification

# Configuração opcional para deixar o painel da Empresa mais bonito e exibir o hash gerado
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hash')
    readonly_fields = ('hash',)  # O hash é gerado automaticamente, então deixamos apenas como leitura

# Registra o Target
@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'user_id')
    list_filter = ('empresa',)

# Registra a Notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('target', 'mensagem', 'is_read', 'criado_em')
    list_filter = ('is_read', 'target__empresa')
    search_fields = ('mensagem',)