# Generated by Django 4.1.3 on 2022-12-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbo', '0003_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
