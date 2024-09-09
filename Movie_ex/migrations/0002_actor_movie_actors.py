# Generated by Django 5.1.1 on 2024-09-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_ex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Актеры',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='Movie_ex.actor', verbose_name='актеры'),
        ),
    ]
