
from django.shortcuts import render, redirect
from datetime import datetime, timezone
from tema_31.models import Movie
from root import CONST


def add_movies(request):
    """populare tabela movie."""
    movies = [
        {
            'name_movie': 'The Lord of the Rings',
            'director': 'Peter Jackson',
            'rating': 9,
            'storyline': 'An ancient Ring thought lost for centuries has been found, and through a strange twist of fate has been given to a small Hobbit named Frodo. When Gandalf discovers the Ring is in fact the One Ring of the Dark Lord Sauron, Frodo must make an epic quest to Mount Doom in order to destroy it. However, he does not go alone. He is joined by Gandalf, Legolas the elf, Gimli the Dwarf, Aragorn, Boromir, and his three Hobbit friends Merry, Pippin, and Samwise. Through mountains, snow, darkness, forests, rivers and plains, facing evil and danger at every corner the Fellowship of the Ring must go. Their quest to destroy the One Ring is the only hope for the end of the Dark Lords reign',
            'release_date': datetime(2001, 8, 1, tzinfo=timezone.utc)
        },
        {
            'name_movie': 'Dune: Part One',
            'director': 'Denis Villeneuve',
            'rating': 8,
            'storyline': 'A mythic and emotionally charged hero s journey, Dune tells the story of Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, who must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet s exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity s greatest potential-only those who can conquer their fear will survive',
            'release_date': datetime(2021, 8, 1, tzinfo=timezone.utc)
        },
        {
            'name_movie': 'Venom',
            'director': 'Ruben Fleischer',
            'rating': 7,
            'storyline': 'After a faulty interview with the Life Foundation ruins his career, former reporter Eddie Brock s life is in pieces. Six months later, he comes across the Life Foundation again, and he comes into contact with an alien symbiote and becomes Venom, a parasitic antihero.',
            'release_date': datetime(2018, 8, 1, tzinfo=timezone.utc)
        },
        {
            'name_movie': 'Peaky Blinders',
            'director': 'Steven Knight',
            'rating': 9,
            'storyline': 'Thomas Shelby and his brothers return to Birmingham after serving in the British Army during WWI. After the war, Shelby and his gang, the Peaky Blinders, control the city of Birmingham. However, Shelby s ambitions extend beyond Birmingham, as he plans to build on the business empire that he s created and dispatch anyone who gets in his way.',
            'release_date': datetime(2013, 8, 1, tzinfo=timezone.utc)
        }
    ]

    for movie in movies:
        Movie.objects.create(**movie)

    return redirect('movies')


def movies(request):
    """randare template exercitiu.html."""
    all_movies = Movie.objects.all()
    context = {
        'titlu': CONST['nr_tema_31'],
        'version': CONST['version'],
        'movies': all_movies,
    }
    return render(request, 'tema_31/exercitiu.html', context)
