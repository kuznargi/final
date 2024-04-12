from django.contrib.auth.models import User 
def users(request):
     user = None
     if request.user.is_authenticated:
          user=request.user
        
     return {'user': user}
