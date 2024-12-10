# Generated by Django 5.1.3 on 2024-11-25 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='ping',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='pings', to='pings.tag'),
        ),
    ]
