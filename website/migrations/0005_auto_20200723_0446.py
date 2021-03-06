# Generated by Django 3.0.8 on 2020-07-23 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200723_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentation',
            name='categorie_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Category_product'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='prix',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('google-plus', 'fa-google-plus-g'), ('rss', 'fa-rss'), ('instagram', 'fa-instagram'), ('flickr', 'fa-flickr'), ('linkedin', 'fa-linkedin-in'), ('facebook', 'fa-facebook'), ('dribble', 'fa-dribbble'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]
