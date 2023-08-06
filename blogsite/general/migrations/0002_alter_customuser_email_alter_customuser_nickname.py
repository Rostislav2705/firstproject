# Generated by Django 4.2.1 on 2023-06-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
