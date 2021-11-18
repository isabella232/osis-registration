# Generated by Django 3.2.3 on 2021-08-24 10:28

from django.db import migrations, models


def create_osis_registration_polling_subscriber(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    PollingSubscriber = apps.get_model('base', 'PollingSubscriber')
    PollingSubscriber.objects.create(
        app_name=User.objects.create(username='osis_registration')
    )


def delete_osis_registration_polling_subscriber(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    PollingSubscriber = apps.get_model('base', 'PollingSubscriber')
    PollingSubscriber.objects.get(app_name__username='osis_registration').delete()
    User.objects.get(username='osis_registration').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_useraccountrequestresult_email'),
    ]

    operations = [
        migrations.RunPython(
            code=create_osis_registration_polling_subscriber,
            reverse_code=delete_osis_registration_polling_subscriber
        )
    ]
