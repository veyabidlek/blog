from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = {
        'title':'Career',
        'clubs':['Sporting CF', 'Manchester United FC', 'Real Madrid CF', 'Juventus FC', 'Al-Nassr FC'],
        
    }
    return render(request, 'main/index.html',data)


def stats(request):
    return render(request, 'main/stats.html')

def trophies(request):
    return render(request, 'main/trophies.html')