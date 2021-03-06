# Generated by Django 3.2.7 on 2022-05-03 13:57

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0003_alter_pollingunit_lga_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='polling_unit_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='ward_id', chained_model_field='uniquewardid', on_delete=django.db.models.deletion.CASCADE, to='Election.pollingunit'),
        ),
        migrations.AlterField(
            model_name='pollingunit',
            name='uniquewardid',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='lga_id', chained_model_field='lga_id', on_delete=django.db.models.deletion.CASCADE, to='Election.ward'),
        ),
    ]
