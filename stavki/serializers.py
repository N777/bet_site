from stavki.models import Catalog, Orders


def catalog_to_dict(o: Catalog) -> dict:
    return {
        'id': o.pk,
        'enemy_f': o.enemy_f,
        'enemy_s': o.enemy_s,
        'rate': o.rate,
        'end': o.end,
        'result': o.result
    }


def choice_to_name(bet: dict, choice: int) -> str:
    if bool(choice):
        return bet.get('enemy_s')
    else:
        return bet.get('enemy_f')


def order_to_dict(o: Orders) -> dict:
    bet = catalog_to_dict(o.catalog)
    return {
        'id': o.pk,
        'catalog': bet,
        'choice': choice_to_name(bet, o.choice),
        'user': "Игорь",
        'order_sum': o.order_sum
    }


def orders_to_list(orders: list) -> list:
    list_orders = []
    for order in orders:
        list_orders.append(order_to_dict(order))
    return list_orders
