# Generated by Django 4.0.4 on 2022-06-25 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputamenity',
            name='big_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='birthday_amenity',
            field=models.CharField(blank=True, choices=[('Happy Birthday', 'Happy Birthday'), ('Happy Aniversary', 'Happy Amiversary'), ('Congartulations', 'Congratulations')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='dessert_amenity',
            field=models.CharField(blank=True, choices=[('Macaroons 4pcs', 'Macaroons 4pcs'), ('Baklava', 'Baklava'), ('Maamul', 'Maamul'), ('Macaroons 8pcs', 'Macaroons 8pcs'), ('Arab amenity', 'Arab amenity'), ('Chocolate truffle', 'Chocolate truffle')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='drink_amenity',
            field=models.CharField(blank=True, choices=[('Red wine', 'Red wine'), ('Negroni', 'Negroni'), ('Champagne', 'Champagne'), ('White wine', 'White wine'), ('Water', 'Water')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='fruit_amenity',
            field=models.CharField(blank=True, choices=[('Midium fruit', 'Midium fruit'), ('Large fruit', 'Large fruit'), ('Presidential', 'Presidential'), ('Small fruit', 'Small fruit')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inputamenity',
            name='month',
            field=models.CharField(choices=[('February', 'February'), ('May', 'May'), ('August', 'August'), ('September', 'September'), ('June', 'June'), ('Octomber', 'Octomber'), ('January', 'January'), ('April', 'April'), ('March', 'March'), ('July', 'July'), ('December', 'December')], max_length=300),
        ),
    ]