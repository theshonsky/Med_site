# Generated by Django 4.1.7 on 2023-04-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mkb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Номер')),
                ('name', models.TextField(verbose_name='Наименование')),
                ('code', models.CharField(max_length=15, verbose_name='Код')),
                ('parent_id', models.IntegerField(null= True, verbose_name='Номер родителя')),
                ('parent_code', models.CharField(null= True, max_length=15, verbose_name='Код родителя')),
                ('node_count', models.IntegerField(default=0, verbose_name='Количество')),
                ('additional_info', models.TextField(null= True, verbose_name='Дополнительная информация')),
            ],
        ),
    ]
