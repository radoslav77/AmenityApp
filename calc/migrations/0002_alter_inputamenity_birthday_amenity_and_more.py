# Generated by Django 4.0.4 on 2022-05-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputamenity',
            name='birthday_amenity',
            field=models.CharField(choices=[('Happy Birthday', 'Happy Birthday'), ('Congartulations', 'Congratulations'), ('Happy Aniversary', 'Happy Amiversary')], default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='dessert_amenity',
            field=models.CharField(choices=[('Macaroons 4pcs', 'Macaroons 4pcs'), ('Arab amenity', 'Arab amenity'), ('Macaroons 8pcs', 'Macaroons 8pcs'), ('Maamul', 'Maamul'), ('Chocolate truffle', 'Chocolate truffle'), ('Baklava', 'Baklava')], default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='drink_amenity',
            field=models.CharField(choices=[('White wine', 'White wine'), ('Negroni', 'Negroni'), ('Champagne', 'Champagne'), ('Red wine', 'Red wine'), ('Water', 'Water')], max_length=200),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='fruit_amenity',
            field=models.CharField(choices=[('Midium fruit', 'Midium fruit'), ('Presidential', 'Presidential'), ('Large fruit', 'Large fruit'), ('Small fruit', 'Small fruit')], max_length=200),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='guests_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='returns',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='vip_level',
            field=models.IntegerField(),
        ),
    ]
