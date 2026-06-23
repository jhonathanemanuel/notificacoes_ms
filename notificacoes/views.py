from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from .authentication import get_target_from_headers

class NotificacoesNaoLidasCountView(APIView):
    def get(self, request):
        target = get_target_from_headers(request)
        count = Notification.objects.filter(target=target, is_read=False).count()
        return Response({'count': count})

class NotificacoesListView(APIView):
    def get(self, request):
        target = get_target_from_headers(request)
        notificacoes = Notification.objects.filter(target=target)
        serializer = NotificationSerializer(notificacoes, many=True)
        return Response(serializer.data)

class NotificacaoMarcarLidaView(APIView):
    def patch(self, request, pk):
        target = get_target_from_headers(request)
        try:
            notificacao = Notification.objects.get(pk=pk, target=target)
            notificacao.is_read = True
            notificacao.save()
            return Response(NotificationSerializer(notificacao).data)
        except Notification.DoesNotExist:
            return Response({'erro': 'Não encontrada'}, status=404)