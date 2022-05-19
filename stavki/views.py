from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from stavki.forms import OrderForm, BalanceForm
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


def makeorder(request, catalog_id: int):
    if request.method == 'POST':
        new_order = Orders(catalog_id=catalog_id, choice=bool(int(request.POST.get('choice'))),
                           order_sum=int(request.POST.get('order_sum')), user=request.user)
        request.user.balance -= int(request.POST.get('order_sum'))
        request.user.save()
        new_order.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = OrderForm(initial={'id': catalog_id})
    context = {
        'form': form,
        'order': Catalog.objects.get(pk=catalog_id)
    }
    return render(request, 'stavki/make_order.html', context)


def add_balance(request):
    if request.method == 'POST':
        request.user.balance += int(request.POST.get('sum'))
        request.user.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        form = BalanceForm()
    context = {
        'form': form
    }
    return render(request, 'stavki/add_balance.html', context)
