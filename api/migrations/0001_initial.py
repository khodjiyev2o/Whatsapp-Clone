# Generated by Django 4.0.5 on 2022-07-02 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('first_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_person', to=settings.AUTH_USER_MODEL)),
                ('second_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('first_person', 'second_person'), ('second_person', 'first_person')},
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_thread', to='api.thread')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]