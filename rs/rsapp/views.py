from django.shortcuts import render

def res_view(request):
    return render(request, 'res.html')
