# Generated by Django 4.1.7 on 2023-03-09 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerry', '0002_alter_portfolio_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='user_id',
            field=models.UUIDField(null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
