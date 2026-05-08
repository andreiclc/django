from django.shortcuts import render

def exercitiu(request):
    context = {
        'nume': 'andrei',
        'animale': 5,
    }
    return render(request, 'tema_29/exercitiu.html', context)
