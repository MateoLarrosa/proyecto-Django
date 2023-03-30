# Generated by Django 4.1.7 on 2023-03-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.CharField(max_length=10)),
                ('documento', models.IntegerField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]