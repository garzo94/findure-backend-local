# Generated by Django 4.1.7 on 2023-03-13 21:48

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, default='', max_length=255)),
                ('city', models.CharField(blank=True, default='', max_length=255)),
                ('postal_code', models.IntegerField(default=0)),
                ('country', models.CharField(blank=True, default='', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=api.models.category_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_camino', 'En camino'), ('completada', 'Completada'), ('cancelada', 'Cancelada')], default='pendiente', max_length=200)),
                ('delivery_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shippingPrice', models.FloatField(default=0.0)),
                ('totalPrice', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('rating', models.FloatField()),
                ('price', models.FloatField()),
                ('description', models.CharField(blank=True, default='', max_length=500)),
                ('recently_added', models.BooleanField(default=False)),
                ('best_seller', models.BooleanField(default=False)),
                ('best_seller_image', models.ImageField(blank=True, null=True, upload_to=api.models.bestseller_path)),
                ('image', models.ImageField(upload_to=api.models.product_directory_path)),
                ('favorite_by', models.ManyToManyField(blank=True, related_name='favorite_products', to=settings.AUTH_USER_MODEL)),
                ('franchise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.franchise')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('review', models.CharField(max_length=250)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
