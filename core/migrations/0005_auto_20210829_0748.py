# Generated by Django 3.2.6 on 2021-08-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_globaluser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpamScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(blank=True, db_index=True)),
                ('spam_score', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='globaluser',
            name='spam_score',
        ),
    ]
