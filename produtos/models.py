from django.db import models


class Produtos(models.Model):
    name = models.CharField("Name", max_length=100)
    preco = models.DecimalField("Preco", max_digits=4, decimal_places=2)
    ativo = models.BooleanField("Ativo", default=False)


# >>> car2 = Produtos.objects.create(name="car2", preco=31.9)
# >>> for produtos in Produtos.objects.all():
# ...     print(produtos.name)

# >>> for produtos in Produtos.objects.filter(name="2"):
# >>> for produtos in Produtos.objects.filter(name__contains="2"):
# >>> for produtos in Produtos.objects.filter(name__in=["2"]):

