# Generated by Django 4.0.4 on 2022-12-11 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0006_alter_inputamenity_dessert_amenity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputamenity',
            name='birthday_amenity',
            field=models.CharField(blank=True, choices=[('Happy Aniversary', 'Happy Amiversary'), ('Happy Birthday', 'Happy Birthday'), ('Congartulations', 'Congratulations')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='dessert_amenity',
            field=models.CharField(blank=True, choices=[('Macaroons 4pcs', 'Macaroons 4pcs'), ('Macaroons 8pcs', 'Macaroons 8pcs'), ('Baklava', 'Baklava'), ('Arab amenity', 'Arab amenity'), ('Maamul', 'Maamul'), ('Chocolate truffle', 'Chocolate truffle')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('Water', 'Water'), ('White wine', 'White wine'), ('Red wine', 'Red wine'), ('Champagne', 'Champagne'), ('Negroni', 'Negroni')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='fruit_amenity',
            field=models.CharField(blank=True, choices=[('Presidential', 'Presidential'), ('Midium fruit', 'Midium fruit'), ('Small fruit', 'Small fruit'), ('Large fruit', 'Large fruit')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='month',
            field=models.CharField(choices=[('June', 'June'), ('September', 'September'), ('December', 'December'), ('Octomber', 'Octomber'), ('July', 'July'), ('January', 'January'), ('May', 'May'), ('August', 'August'), ('February', 'February'), ('November', 'November'), ('April', 'April'), ('March', 'March')], max_length=300),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='amenity',
            field=models.CharField(choices=[('Lemon cake', 'Lemon cake'), ('Flapjack', 'Flapjack'), ('Madleines', 'Madleines'), ('Pistachio Finnacier', 'Pistachio Finnacier'), ('Florentine', 'Florebntine'), ('Macaroons', 'Macaroons')], max_length=200),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('Water', 'Water'), ('White wine', 'White wine'), ('Red wine', 'Red wine'), ('Champagne', 'Champagne'), ('Negroni', 'Negroni')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='month',
            field=models.CharField(choices=[('June', 'June'), ('September', 'September'), ('December', 'December'), ('Octomber', 'Octomber'), ('July', 'July'), ('January', 'January'), ('May', 'May'), ('August', 'August'), ('February', 'February'), ('November', 'November'), ('April', 'April'), ('March', 'March')], max_length=300),
        ),
    ]