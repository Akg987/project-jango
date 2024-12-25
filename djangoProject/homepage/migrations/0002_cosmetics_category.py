# Generated by Django 5.1 on 2024-09-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cosmetics',
            name='category',
            field=models.CharField(choices=[('SKINCARE', 'Skincare'), ('MAKEUP', 'Makeup'), ('FRAGRANCE', 'Fragrance'), ('HAIRCARE', 'Haircare'), ('BODYCARE', 'Bodycare')], default='SKINCARE', max_length=20),
        ),
    ]