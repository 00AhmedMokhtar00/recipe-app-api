# Generated by Django 3.2.18 on 2023-04-29 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='tst_dft', max_length=255),
            preserve_default=False,
        ),
    ]
