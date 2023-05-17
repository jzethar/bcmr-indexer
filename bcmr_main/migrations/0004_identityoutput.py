# Generated by Django 3.1.6 on 2023-05-17 06:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bcmr_main', '0003_auto_20230514_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentityOutput',
            fields=[
                ('tx_hash', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('authbase', models.BooleanField(default=False)),
                ('genesis', models.BooleanField(default=False)),
                ('spent', models.BooleanField(default=False)),
                ('burned', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identity_output', to='bcmr_main.token')),
            ],
            options={
                'ordering': ('-date_created', 'token'),
            },
        ),
    ]