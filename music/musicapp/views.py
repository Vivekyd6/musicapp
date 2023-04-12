from django.shortcuts import render
import requests

# Create your views here.
def search(request):
      return render(request , 'search.html')


def search_results(request):
     term = request.GET.get('term')
     url = 'https://itunes.apple.com/search'
     params = {'term':term, 'media':'music','entity':'album'}
     response = requests.get(url, params=params)
     results = response.json()['results']
     return render(request, 'search_results.html',{'results':results,'term':term,})
     