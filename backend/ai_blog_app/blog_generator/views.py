from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        link = data.get('link')
        # ... votre logique IA ici
        return JsonResponse({'content': f'Blog généré pour {link}'})
    return JsonResponse({'error': 'Méthode invalide'}, status=405)
