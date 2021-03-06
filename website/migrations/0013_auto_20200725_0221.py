# Generated by Django 3.0.8 on 2020-07-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20200723_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_products',
            old_name='prix',
            new_name='prix1',
        ),
        migrations.AddField(
            model_name='our_products',
            name='prix2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('linkedin', 'fa-linkedin-in'), ('dribble', 'fa-dribbble'), ('pinterest', 'fa-pinterest'), ('rss', 'fa-rss'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('google-plus', 'fa-google-plus-g'), ('instagram', 'fa-instagram')], max_length=20, null=True),
        ),
    ]
