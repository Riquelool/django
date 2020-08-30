# Generated by Django 3.0.7 on 2020-08-28 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reasson', models.CharField(blank=True, default='', max_length=255, verbose_name='raison')),
                ('date', models.DateField(verbose_name='data')),
                ('ismissing', models.BooleanField(default=True)),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.Student')),
            ],
        ),
    ]