from django.contrib import admin

# Register your models here.
from stavki.models import Catalog, Orders, Users

admin.site.register(Catalog)
admin.site.register(Orders)
admin.site.register(Users)
