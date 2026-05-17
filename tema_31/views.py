from django.shortcuts import render

def movie(request):
    return render(request, 'tema_31/exercitiu.html', {})