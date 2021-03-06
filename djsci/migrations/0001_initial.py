# Generated by Django 2.1.1 on 2018-09-17 05:58

from django.db import migrations, models
import django.db.models.deletion
import djsci.fields
import knob.dt


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('uri', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('desc', models.TextField(blank=True, default='', null=True)),
                ('create_dt', models.DateTimeField(default=knob.dt.local_now)),
                ('update_dt', models.DateTimeField(default=knob.dt.local_now)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('desc', models.TextField(blank=True, default='', null=True)),
                ('data', djsci.fields.DataField(blank=True, editable=False, null=True)),
                ('create_dt', models.DateTimeField(default=knob.dt.local_now)),
                ('update_dt', models.DateTimeField(default=knob.dt.local_now)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variables', to='djsci.Basket')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='variable',
            unique_together={('basket', 'name')},
        ),
    ]
