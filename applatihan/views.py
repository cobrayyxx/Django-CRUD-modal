from django.shortcuts import render
from django.http import HttpResponse
import requests 

# Create your views here.

# Hit GET API
def index(request):
    response = requests.get("https://rontia-rg1.aiseeyou.tech/reference/news")
    news = response.json()


    
    return render(request, 'index.html', {
        # 'title' : news['result'][0]['json_data']['articles'][0]['title'],
        # 'description' : news['result'][0]['json_data']['articles'][0]['description']
      'news' : news
    })


  