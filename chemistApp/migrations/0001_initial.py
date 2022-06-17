# Generated by Django 4.0.5 on 2022-06-17 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chemist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact_no', models.CharField(max_length=255)),
                ('chemist_email', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('sname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=15)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('requets_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=25)),
                ('medicine_details', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=25)),
                ('sname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('phone_no', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(max_length=255)),
                ('medicine_type', models.CharField(max_length=255)),
                ('buy_price', models.CharField(max_length=25)),
                ('sell_price', models.CharField(max_length=25)),
                ('exp_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('instock_qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApp.chemist')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalDetails',
            fields=[
                ('medical_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=255)),
                ('salt_qty', models.CharField(max_length=25)),
                ('salt_type', models.CharField(max_length=25)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApp.medicine')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('bill_details_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApp.bill')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApp.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemistApp.customer'),
        ),
    ]