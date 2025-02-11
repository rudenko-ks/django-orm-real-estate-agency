# Generated by Django 2.2.24 on 2022-11-05 22:19

from django.db import migrations
from django.db.models import F


def set_flatowners_relation(apps, scheme_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all().iterator():
        flat.owners.set(
            Owner.objects.filter(owner_fullname=flat.owner,
                                 owners_phonenumber=flat.owners_phonenumber))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221106_0024'),
    ]

    operations = [
        migrations.RunPython(set_flatowners_relation),
    ]
