# Generated by Django 3.0.8 on 2020-07-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20200723_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_products',
            old_name='nom',
            new_name='titre',
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('dribble', 'fa-dribbble'), ('rss', 'fa-rss'), ('google-plus', 'fa-google-plus-g'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('instagram', 'fa-instagram'), ('linkedin', 'fa-linkedin-in'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]
