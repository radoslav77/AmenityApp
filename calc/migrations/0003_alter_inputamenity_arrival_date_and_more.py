# Generated by Django 4.0.4 on 2022-06-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_alter_inputamenity_big_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputamenity',
            name='arrival_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='birthday_amenity',
            field=models.CharField(blank=True, choices=[('Congartulations', 'Congratulations'), ('Happy Birthday', 'Happy Birthday'), ('Happy Aniversary', 'Happy Amiversary')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='dessert_amenity',
            field=models.CharField(blank=True, choices=[('Macaroons 8pcs', 'Macaroons 8pcs'), ('Maamul', 'Maamul'), ('Baklava', 'Baklava'), ('Macaroons 4pcs', 'Macaroons 4pcs'), ('Arab amenity', 'Arab amenity'), ('Chocolate truffle', 'Chocolate truffle')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('Negroni', 'Negroni'), ('White wine', 'White wine'), ('Champagne', 'Champagne'), ('Water', 'Water'), ('Red wine', 'Red wine')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='month',
            field=models.CharField(choices=[('July', 'July'), ('December', 'December'), ('January', 'January'), ('September', 'September'), ('May', 'May'), ('February', 'February'), ('Octomber', 'Octomber'), ('August', 'August'), ('April', 'April'), ('March', 'March'), ('June', 'June')], max_length=300),
        ),
    ]
