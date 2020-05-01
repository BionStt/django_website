from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from git_book.models import Subscription


@method_decorator(csrf_exempt, name='dispatch')
class SubscribeGitView(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email', None)
        if email:
            if Subscription.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Already signed up'})
            Subscription.objects.create(email=email)
            response =  JsonResponse({'message': 'Thank you for signing up!'})
            response['Access-Control-Allow-Origin'] = '*'
            return response

        return HttpResponse(status=400)

