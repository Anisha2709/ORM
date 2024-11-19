# Generated by Django 4.2.16 on 2024-11-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_acno', models.IntegerField()),
                ('cust_name', models.CharField(max_length=100)),
                ('loan_amt', models.FloatField()),
                ('loan_type', models.CharField(max_length=100)),
            ],
        ),
    ]