# Generated by Django 4.1.3 on 2024-08-12 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fires', '0003_wildfire_wildfiredetail_delete_firereport_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WildfireReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('summary', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='wildfiredetail',
            name='wildfire',
        ),
        migrations.DeleteModel(
            name='Wildfire',
        ),
        migrations.DeleteModel(
            name='WildfireDetail',
        ),
    ]
