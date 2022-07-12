# Generated by Django 4.0 on 2022-06-29 17:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='users.user')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
