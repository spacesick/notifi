# Generated by Django 4.1.7 on 2023-04-02 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0018_improve_crontab_helptext'),
        ('listing', '0005_alter_listing_content_hash_alter_listing_scheduler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='content_hash',
            field=models.IntegerField(blank=True, editable=False, help_text='The hash of the latest website content that has been checked', null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='scheduler',
            field=models.OneToOneField(blank=True, editable=False, help_text='The scheduler for this listing', null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask'),
        ),
    ]