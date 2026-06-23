from rest_framework.exceptions import AuthenticationFailed
from .models import Empresa, Target

def get_target_from_headers(request):
    api_key = request.headers.get('X-Api-Key')
    user_id = request.headers.get('X-User-Id')

    if not api_key or not user_id:
        raise AuthenticationFailed('Headers X-Api-Key e X-User-Id são obrigatórios.')

    try:
        empresa = Empresa.objects.get(hash=api_key)
    except Empresa.DoesNotExist:
        raise AuthenticationFailed('X-Api-Key inválida.')

    target, created = Target.objects.get_or_create(
        empresa=empresa,
        user_id=int(user_id)
    )
    return target