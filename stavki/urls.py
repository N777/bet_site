from django.urls import path

from stavki import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makeorder/<int:catalog_id>', views.makeorder, name='makeorder'),
    path('add-balance', views.add_balance, name='add-balance')
]
#/<int:catalog_id>/<int:side>/<int:sum>