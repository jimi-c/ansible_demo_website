from django.contrib.auth.models import User
from django.http import HttpResponse

def health(request):
    try:
        User.objects.count()
        return HttpResponse("ok")
    except:
        return HttpResponse(status=500)
