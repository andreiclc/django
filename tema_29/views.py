from django.shortcuts import render
from root import CONST

def exercitiu(request):
    context = {
        'nume': 'andrei',
        'animale': 5,
        'titlu': CONST['nr_tema'],
        'version': CONST['version'],
    }
    return render(request, 'tema_29/exercitiu.html', context)
