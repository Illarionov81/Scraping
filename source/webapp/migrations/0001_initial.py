# Generated by Django 3.2.2 on 2021-05-12 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Company')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('open', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Open')),
                ('high', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='High')),
                ('low', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Low')),
                ('close', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Close')),
                ('adj_close', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='Adj Close')),
                ('volume', models.IntegerField(verbose_name='Volume')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='webapp.company', verbose_name='company')),
            ],
        ),
    ]
