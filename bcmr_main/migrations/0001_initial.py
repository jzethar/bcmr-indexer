# Generated by Django 3.1.6 on 2023-06-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('txid', models.CharField(max_length=255, unique=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('valid', models.BooleanField(default=False)),
                ('op_return', models.TextField(default='')),
                ('bcmr_url', models.TextField(default='')),
                ('bcmr_request_status', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Registries',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('txid', models.CharField(blank=True, max_length=255, null=True)),
                ('is_nft', models.BooleanField(default=False)),
                ('commitment', models.CharField(blank=True, max_length=255, null=True)),
                ('capability', models.CharField(blank=True, choices=[('minting', 'Minting'), ('mutable', 'Mutable'), ('none', 'None')], max_length=20, null=True)),
                ('bcmr_url', models.URLField(blank=True, max_length=255, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-updated_at',),
                'unique_together': {('category', 'commitment', 'capability')},
            },
        ),
        migrations.CreateModel(
            name='IdentityOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(max_length=255, unique=True)),
                ('parent_txid', models.CharField(max_length=255, unique=True)),
                ('block', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('authbase', models.BooleanField(default=False)),
                ('genesis', models.BooleanField(default=False)),
                ('spent', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('spender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bcmr_main.identityoutput')),
            ],
            options={
                'verbose_name_plural': 'Identity Outputs',
                'ordering': ('-date',),
            },
        ),
    ]
