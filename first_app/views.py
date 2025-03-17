import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'changhee'

    context = {
        'my_name': my_name,
    }
    return render(request, 'hello.html', context)

def lunch(request):
    menu = ['김밥', '커리', '타코']

    pick = random.choice(menu)

    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    
    lucky_numbers = random.sample(range(1, 46), 6)

    context = {
        'lucky_numbers': lucky_numbers,
    }

    return render(request, 'lotto.html', context)

def profile(request, username):
    context = {
        'username': username,
    }
    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'number': number,
        'result': result,
    }

    return render(request, 'cube.html', context)