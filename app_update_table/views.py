from http.client import responses
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres_conn import atualizar 


@api_view(['PUT'])
def update_table(request):
    
    try:
        data = JSONParser().parse(request)
        # for chave in data.keys():
        #     lista.append(chave + '= ')
        #     for valor in data.items():
        #         lista.append(valor + ', ')       
        #coluna = list(data.keys())[0]
        email = data['email']     
        atualizar(data)
        return JsonResponse(email, status=201, safe=False)

    except Exception as ex:
        response = {
            "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)