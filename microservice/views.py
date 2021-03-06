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
                data['email'] = emails

                # ищем ФИО
                last_names = re.findall(re_lastname, content)
                data['lastname'] = last_names

                # ищем компании
                company = re.findall(re_company, content)
                data['company'] = company

                data['negative_header'] = []

                for key in data.keys():
                    if key == 'url':
                        continue
                    for value in data[key]:
                        url_data = UrlData()
                        url_data.url = url
                        setattr(url_data, key, value)

                        if UrlData.objects.filter(**{key: value}).exists():
                            continue
                        url_data.save()

                return Response(data)
            else:
                return Response({'error': 'Неверный ключ'}, status=401)
        else:
            return Response({'error': 'Неверный ключ'}, status=401)


@api_view(['GET'])
def micro_service2(request):
    if request.method == 'GET':
        if request.query_params.get('key'):
            if request.query_params['key'] == key_access:
                lastname = request.query_params.get('lastname')

                if lastname is None:
                    return Response(status=400)
                else:
                    query_url = UrlData.objects.raw("""
                        SELECT * FROM microservice_urldata 
                        JOIN microservice_urldata ms ON microservice_urldata.url=ms.url
                        WHERE microservice_urldata.lastname='%s'
                        GROUP BY microservice_urldata.url
                    """ % (lastname))

                    urls = [i.url for i in query_url]

                    return Response({"urls": urls})
            else:
                return Response({'error': 'Неверный ключ'}, status=401)
        else:
            return Response({'error': 'Неверный ключ'}, status=401)
