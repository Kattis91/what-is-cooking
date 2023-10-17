# Generated by Django 3.2 on 2023-10-16 23:05

import blog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20231012_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='estimated_time',
            field=models.PositiveIntegerField(validators=[blog.models.validate_nonzero, django.core.validators.MaxValueValidator(600)], verbose_name='estimated_time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(validators=[blog.models.validate_nonzero, django.core.validators.MaxValueValidator(50)], verbose_name='servings'),
        ),
    ]