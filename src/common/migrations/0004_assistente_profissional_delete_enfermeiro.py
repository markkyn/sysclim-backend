# Generated by Django 4.2.11 on 2024-04-04 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_assistente_email_remove_assistente_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistente',
            name='profissional',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Enfermeiro',
        ),
    ]
