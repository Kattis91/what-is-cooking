# Generated by Django 3.2 on 2023-10-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231002_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=4, verbose_name='servings'),
        ),
    ]
