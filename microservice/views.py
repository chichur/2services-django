import re
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .regexps import re_email, re_lastname, re_company
from .models import UrlData

# Create your views here.

# ключ доступа к сервису
key_access = '123456789'


@api_view(['GET'])
def micro_service1(request):
    if request.method == 'GET':
        if request.query_params.get('key'):
            if request.query_params['key'] == key_access:
                url = request.query_params['url']
                try:
                    req_url = requests.get(url)
                except:
                    return Response({'error': 'Неверный url'}, status=400)

                data = {'url': url}
                content = str(req_url.text)

                # ищем эмэилы
                emails = re.findall(re_email, content)
                data['emails'] = emails

                # ищем ФИО
                last_names = re.findall(re_lastname, content)
                data['last_names'] = last_names

                # ищем компании
                company = re.findall(re_company, content)
                data['company'] = company

                for value in data['emails']:
                    url_data = UrlData()
                    url_data.url = url
                    url_data.email = value
                    url_data.save()

                for value in data['last_names']:
                    url_data = UrlData()
                    url_data.url = url
                    url_data.lastname = value
                    url_data.save()

                for value in data['company']:
                    url_data = UrlData()
                    url_data.url = url
                    url_data.company = value
                    url_data.save()

                return Response(data)
            else:
                return Response({'error': 'Неверный ключ'}, status=401)
        else:
            return Response({'error': 'Неверный ключ'}, status=401)


@api_view(['GET'])
def micro_service2(request):
    if request.method == 'GET':
        return Response(request.query_params)
