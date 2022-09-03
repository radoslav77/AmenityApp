# Generated by Django 4.0.4 on 2022-09-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_inputamenity_num_of_dessert_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputamenity',
            name='dessert_amenity',
            field=models.CharField(blank=True, choices=[('Macaroons 8pcs', 'Macaroons 8pcs'), ('Maamul', 'Maamul'), ('Arab amenity', 'Arab amenity'), ('Baklava', 'Baklava'), ('Macaroons 4pcs', 'Macaroons 4pcs'), ('Chocolate truffle', 'Chocolate truffle')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('White wine', 'White wine'), ('Champagne', 'Champagne'), ('Water', 'Water'), ('Negroni', 'Negroni'), ('Red wine', 'Red wine')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='fruit_amenity',
            field=models.CharField(blank=True, choices=[('Midium fruit', 'Midium fruit'), ('Large fruit', 'Large fruit'), ('Presidential', 'Presidential'), ('Small fruit', 'Small fruit')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('September', 'September'), ('March', 'March'), ('July', 'July'), ('May', 'May'), ('April', 'April'), ('December', 'December'), ('August', 'August'), ('June', 'June'), ('Octomber', 'Octomber'), ('February', 'February')], max_length=300),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='num_of_drink',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='amenity',
            field=models.CharField(choices=[('Flapjack', 'Flapjack'), ('Macaroons', 'Macaroons'), ('Lemon cake', 'Lemon cake'), ('Madleines', 'Madleines'), ('Florentine', 'Florebntine'), ('Pistachio Finnacier', 'Pistachio Finnacier')], max_length=200),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('White wine', 'White wine'), ('Champagne', 'Champagne'), ('Water', 'Water'), ('Negroni', 'Negroni'), ('Red wine', 'Red wine')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='longstay',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('September', 'September'), ('March', 'March'), ('July', 'July'), ('May', 'May'), ('April', 'April'), ('December', 'December'), ('August', 'August'), ('June', 'June'), ('Octomber', 'Octomber'), ('February', 'February')], max_length=300),
        ),
    ]
