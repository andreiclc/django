from django.shortcuts import render
from root import CONST

def exercitiu(request):
    """randare template exercitiu.html."""
    context = {
        'nume': 'andrei',
        'animale': 5,
        'titlu': CONST['nr_tema_29'],
        'version': CONST['version'],
    }
    return render(request, 'tema_29/exercitiu.html', context)
