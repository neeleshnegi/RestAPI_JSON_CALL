from django.shortcuts import render,HttpResponse
import requests
# Create your views here.

def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    print(users)

    return render(request,'restapi/index.html',{'users':users})