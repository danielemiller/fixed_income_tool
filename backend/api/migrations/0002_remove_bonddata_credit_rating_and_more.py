# Generated by Django 4.2 on 2023-04-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonddata',
            name='credit_rating',
        ),
        migrations.RemoveField(
            model_name='bonddata',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='bonddata',
            name='yield_to_maturity',
        ),
        migrations.AddField(
            model_name='bonddata',
            name='current_yield',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bonddata',
            name='face_value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AddField(
            model_name='bonddata',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='bonddata',
            name='ytm',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bonddata',
            name='coupon_rate',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='bonddata',
            name='issuer',
            field=models.CharField(max_length=200),
        ),
    ]