import secrets
from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    hash = models.CharField(max_length=16, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = secrets.token_hex(8) # Gera a API Key aleatória de 16 caracteres
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Target(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='targets')
    user_id = models.IntegerField() # Apenas o número do ID do usuário lá no portfólio

    class Meta:
        unique_together = ['empresa', 'user_id']

    def __str__(self):
        return f'{self.empresa.nome} - User {self.user_id}'

class Notification(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='notificacoes')
    mensagem = models.TextField()
    is_read = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']