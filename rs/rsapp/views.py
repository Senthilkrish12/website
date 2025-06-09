from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hi Krishna, welcome to your website!</h1>")
