# Generated by Django 3.2.3 on 2021-07-14 09:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('osis_registration', '0003_auto_20210713_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccountcreationrequest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='useraccountdeletionrequest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='useraccountrenewalrequest',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
