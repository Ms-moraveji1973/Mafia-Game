# Generated by Django 5.0.6 on 2024-07-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mafia', '0003_mafiarolemodel_name_alter_mafiarolemodel_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('cart', models.CharField(choices=[('silence', 'Silence'), ('face_off', 'Face_Off'), ('imagin', 'Imagin'), ('person', 'Person'), ('dastband', 'Dastband')], max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Player',
        ),
        migrations.AlterField(
            model_name='mafiarolemodel',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]
