from django.shortcuts import render, HttpResponse
import django.http.request
import json
from django.views.decorators.csrf import csrf_exempt
from produtos.models import Produtos

#disponibilizar os dados para o navegador
def list_produtos(request):
    # ler os registros do banco 
    produtos = []
    # converter os registros para json
    for produto in Produtos.objects.all():
        produtos_json = {
            "name": produto.name,
            "preco": float(produto.preco),
            "ativo": produto.ativo,
        }
        produtos.append(produtos_json)
    produtos_json = json.dumps(produtos)
    # responder a requisição
    return HttpResponse(produtos_json, content_type="application/json")

@csrf_exempt
def criar_produtos(request):
    produto = json.loads(request.body)
    novo_produto = Produtos.objects.create(**produto)
    response_body = {
        "id": novo_produto.pk
    }
    return HttpResponse(
        json.dumps(response_body),
        content_type="application/json", 
        status=201)

@csrf_exempt
def atualiza_produto(request, produto_id):
    print(produto_id)
    if request.method in ['PUT', 'POST']:
        return HttpResponse(
            content_type="application/json", status=201)
    return HttpResponse(
            content_type="application/json", status=405)