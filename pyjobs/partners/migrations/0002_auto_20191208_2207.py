# Generated by Django 2.2.7 on 2019-12-08 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("partners", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="company_address",
            field=models.URLField(max_length=500, verbose_name="Site da empresa"),
        ),
        migrations.AlterField(
            model_name="partner",
            name="company_name",
            field=models.CharField(max_length=500, verbose_name="Nome da empresa"),
        ),
        migrations.AlterField(
            model_name="partner",
            name="description",
            field=models.TextField(verbose_name="Descrição da empresa"),
        ),
        migrations.AlterField(
            model_name="partner",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Email da empresa"),
        ),
    ]
