from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from stavki.models import Catalog, Orders, Users
from stavki.serializers import catalog_to_dict, orders_to_list


def index(request):
    catalog = list(Catalog.objects.all())
    catalog_bets = []
    for bet in catalog:
        temp_bet = catalog_to_dict(bet)
        orders_query = Orders.objects.filter(catalog_id=bet.pk)
        orders = orders_to_list(orders_query)
        temp_bet.update({'orders': orders})
        catalog_bets.append(temp_bet)
    context = {
        'catalog': catalog_bets
    }
    return render(request, 'stavki/index.html', context)


def makeorder(request, catalog_id: int, side: int, sum: float):
    user = Users.objects.get(pk=1)
    new_order = Orders(catalog_id=catalog_id, choice=bool(side), order_sum=sum, user=user)
    new_order.save()
    return HttpResponseRedirect(reverse('stavki:index'))
