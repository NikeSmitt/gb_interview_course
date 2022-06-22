from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

from .models import HitCount


def user_hit_count(get_response):
    def middleware(request):
        if not isinstance(request.user, AnonymousUser):
            hc, created = HitCount.objects.get_or_create(user=request.user, url=request.path)
            if not created:
                hc.count += 1
            hc.save()
        
        response = get_response(request)
        
        return response
    
    return middleware
