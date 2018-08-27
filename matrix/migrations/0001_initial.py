# Generated by Django 2.0.7 on 2018-08-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessTokens',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.TextField()),
                ('device_id', models.TextField(blank=True, null=True)),
                ('token', models.TextField(unique=True)),
                ('last_used', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'access_tokens',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True, unique=True)),
                ('password_hash', models.TextField(blank=True, null=True)),
                ('creation_ts', models.BigIntegerField(blank=True, null=True)),
                ('admin', models.SmallIntegerField()),
                ('upgrade_ts', models.BigIntegerField(blank=True, null=True)),
                ('is_guest', models.SmallIntegerField()),
                ('appservice_id', models.TextField(blank=True, null=True)),
                ('consent_version', models.TextField(blank=True, null=True)),
                ('consent_server_notice_sent', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
