import requests
import os
from django.shortcuts import render
from root import CONST

URL = os.getenv('API_URL')


def exercitiu(request):
    """
    - randare template exercitiu.html.
    - request la api ptr a obtine useri.
    - daca api returneaza  400, adauga userii din lista data.
    - afisare useri pe baza unei date de nastere.
    """


    res = requests.get(
        f'{URL}/users',
        params={'number_of_pets': 2}
    )

    if res.status_code == 400:
        data = [
            {'id': 1772, 'name': 'andrei', 'date_of_birth': '2000-05-10', 'number_of_pets': 2},
            {'id': 2773, 'name': 'cosmin', 'date_of_birth': '1999-11-21', 'number_of_pets': 2},
            {'id': 3774, 'name': 'marian', 'date_of_birth': '1999-11-21', 'number_of_pets': 2},
            {'id': 4775, 'name': 'claudiu', 'date_of_birth': '1999-11-21', 'number_of_pets': 4},
        ]

        for user in data:
            requests.post(f'{URL}/users/add', json=user)

        users = data

    else:
        users = res.json()

    res2 = requests.get(
        f'{URL}/users',
        params={
            'date_of_birth': '1999-11-21',
            'number_of_pets': 2
        }
    )

    if res2.status_code == 200:
        users_filtered = res2.json()
    else:
        users_filtered = []

    context = {
        'titlu': CONST['nr_tema_28'],
        'version': CONST['version'],
        'users': users,
        'users_filtered': users_filtered,
    }

    return render(request, 'tema_28/exercitiu.html', context)