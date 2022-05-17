from django.urls import path

from stavki import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makeorder/<int:catalog_id>/<int:side>/<int:sum>', views.makeorder, name='makeorder')
]
