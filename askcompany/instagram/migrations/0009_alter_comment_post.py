# Generated by Django 4.0 on 2021-12-14 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(limit_choices_to={'is_public': True}, on_delete=django.db.models.deletion.CASCADE, to='instagram.post'),
        ),
    ]