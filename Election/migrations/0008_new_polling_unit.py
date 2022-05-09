# Generated by Django 3.2.7 on 2022-05-06 11:39

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0007_auto_20220503_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Polling_Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_name', models.CharField(blank=True, max_length=50, null=True)),
                ('PDP', models.IntegerField()),
                ('DPP', models.IntegerField()),
                ('ACN', models.IntegerField()),
                ('PPA', models.IntegerField()),
                ('CDC', models.IntegerField()),
                ('JP', models.IntegerField()),
                ('ANPP', models.IntegerField()),
                ('LABOUR', models.IntegerField()),
                ('CPP', models.IntegerField()),
                ('lga_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Election.lga')),
                ('ward_name', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='lga_id', chained_model_field='lga_id', on_delete=django.db.models.deletion.CASCADE, to='Election.ward')),
            ],
        ),
    ]