# Generated by Django 4.2.1 on 2023-07-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
