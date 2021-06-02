# Generated by Django 3.2.3 on 2021-05-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReviewId', models.CharField(max_length=120)),
                ('OverallRating', models.FloatField()),
                ('Service', models.IntegerField()),
                ('Cleanliness', models.IntegerField()),
                ('Value', models.IntegerField()),
                ('Location', models.IntegerField()),
                ('Result', models.CharField(max_length=120)),
            ],
        ),
    ]
