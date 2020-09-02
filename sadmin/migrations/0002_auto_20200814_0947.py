# Generated by Django 3.0.8 on 2020-08-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyor',
            name='status',
        ),
        migrations.AddField(
            model_name='surveyor',
            name='designation',
            field=models.CharField(default='nope', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='surveyor',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
