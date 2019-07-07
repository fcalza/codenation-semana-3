from django.contrib import admin
from produtos.models import Produtos

# Register your models here.
class ProdutosModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'preco', 'ativo')
    pass


admin.register(Produtos, ProdutosModelAdmin)
admin.register(Produtos)