from django.dispatch import receiver

from listing.models import Listing

from django.db.models.signals import post_save

import logging


@receiver(post_save, sender=Listing)
def init_scheduler_callback(sender, instance: Listing, created, **kwargs):
    logger = logging.getLogger('django')

    logger.info('here goes your message')   
    if created:
        print("aaaaaaaaaa")
        instance.create_scheduler()
    elif instance.scheduler is not None:
        print("bbbbbbbbbb")
        instance.scheduler.enabled = instance.is_active
        instance.scheduler.save()