# Generated by Django 3.0.8 on 2020-07-23 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200722_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(upload_to='image/categorie')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category product',
                'verbose_name_plural': 'Category product',
            },
        ),
        migrations.CreateModel(
            name='Feeback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(upload_to='image/categorie')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Our_products',
                'verbose_name_plural': 'Our_products',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(upload_to='image/categorie')),
                ('description', models.TextField()),
                ('auteur', models.CharField(max_length=225, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Our_products',
                'verbose_name_plural': 'Our_products',
            },
        ),
        migrations.CreateModel(
            name='Our_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(upload_to='image/categorie')),
                ('prix', models.FloatField(null=True)),
                ('taille_du_cadre', models.PositiveIntegerField(null=True)),
                ('nombre_de_vitesse', models.IntegerField(null=True)),
                ('type_product', models.CharField(max_length=225)),
                ('classe', models.CharField(max_length=225)),
                ('pays', models.CharField(max_length=225)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Our_products',
                'verbose_name_plural': 'Our_products',
            },
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(upload_to='image/categorie')),
                ('description', models.TextField()),
                ('prix', models.FloatField(null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Pub',
                'verbose_name_plural': 'Pub',
            },
        ),
        migrations.CreateModel(
            name='Trouver_le_velo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('type_velo', models.CharField(max_length=255, null=True)),
                ('taille_de_roue', models.PositiveIntegerField(null=True)),
                ('marque', models.CharField(max_length=225, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'trouver le velo',
                'verbose_name_plural': 'trouver le velo',
            },
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='icon',
            field=models.CharField(choices=[('google-plus', 'fa-google-plus-g'), ('rss', 'fa-rss'), ('dribble', 'fa-dribbble'), ('instagram', 'fa-instagram'), ('linkedin', 'fa-linkedin-in'), ('facebook', 'fa-facebook'), ('flickr', 'fa-flickr'), ('pinterest', 'fa-pinterest')], max_length=20, null=True),
        ),
    ]
