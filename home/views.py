from django.shortcuts import render
import requests

# jgIGJAdepGh6vPx47GDpVg==19bkP9q83ZpD5sK2

def index(request):
    check = ""
    if request.method == 'POST':
        API = "jgIGJAdepGh6vPx47GDpVg==19bkP9q83ZpD5sK2"
        name = request.POST['query']
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={name}'
        response = requests.get(api_url, headers={'X-Api-Key': API})

        try:
            if response.status_code == requests.codes.ok:
                check = response.json()
        except Exception as e:
            check = "oops! There was an error" 
            print(e)
        return render (request, 'home.html',{'check':check})      
    else:
        return render(request,'home.html',{'query':'Enter a valid query'})








