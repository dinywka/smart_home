from django.http import HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

@api_view(['GET', 'POST'])
def news(request):
    data1 = requests.get("https://fakenews.squirro.com/news/sport", headers=headers).json()
    _news = data1["news"]
    data2 = []
    for new in _news:
        data2.append({"id": new["id"], "title": new["headline"]})
    return Response(data={"news": data2}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def weather(request):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q=Almaty,kz&APPID="
    api_key = "1e5cfaa68edd16109cd1c6c03c764fab"
    url = BASE_URL + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = int(main["temp"] - 273.15)
        return Response(data={'weather': weather}, status=status.HTTP_200_OK)
    else:
        print('Error')
        return None





