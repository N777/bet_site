from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from stavki.models import Users, Catalog


@receiver(post_save, sender=Catalog)
def my_handler(sender, **kwargs):
    print(sender)
    print(11)