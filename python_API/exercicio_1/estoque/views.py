from django.shortcuts import render
from django.http import JsonResponse

def estoque_view(request,id):
    if request.method == 'GET':
        if id == 1:
            estoque = {
                "id": 1,
                "nome": "vassoura",
                "quantidade": 30,
                "preco": 12.54,
        }
        elif id == 2:
            estoque ={
                "id": 2,
                "nome": "batata",
                "quantidade": 52,
                "preco": 3.99,
            }
        else:
            estoque = {"erro":"produto nao encontrado"}

    return JsonResponse(estoque)

