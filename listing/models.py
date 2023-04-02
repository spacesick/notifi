from django.utils import timezone
import json
from django.db import models

from listing.period import Period
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from django.contrib.auth.models import User

import logging

class Listing(models.Model):
    name = models.CharField(
        max_length=512,
        help_text='The name of this listing',
    )
    url = models.CharField(
        max_length=512,
        help_text='The website URL you want to crawl',
    )
    selector = models.CharField(
        max_length=512,
        help_text='The specific CSS selector for the element you want to watch',
    )
    period = models.IntegerField(
        choices=Period.choices,
        help_text='The time period to check the website',
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Whether this listing is actively being checked or not',
    )
    scheduler = models.OneToOneField(
        PeriodicTask,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # editable=False,
        help_text='The scheduler for this listing',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='The user that created this listing',
    )
    content_hash = models.IntegerField(
        null=True,
        blank=True,
        # editable=False,
        help_text='The hash of the latest website content that has been checked',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text='The creation date of this listing',
    )

    @property
    def interval_schedule(self):
        return IntervalSchedule.objects.get_or_create(every=self.period, period='minutes')[0]

    def create_scheduler(self):
        self.scheduler = PeriodicTask.objects.create(
            name=self.name,
            task='test_task',
            interval=self.interval_schedule,
            args=json.dumps([self.id]),
            start_time=timezone.now()
        )
        self.save()

    def delete(self, *args, **kwargs):
        logger = logging.getLogger('django')
        logger.info('delete') 
        if self.scheduler is not None:
            self.scheduler.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
