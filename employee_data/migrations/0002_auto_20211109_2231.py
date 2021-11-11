# Generated by Django 3.2.8 on 2021-11-09 16:31

from django.db import migrations, models
import django.db.models.deletion
import employee_data.media_path_converter
import utilities.pdf_validator


class Migration(migrations.Migration):

    dependencies = [
        ('employee_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_names', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='em_profile_photo',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='special_document_photo',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_cv',
            field=models.FileField(null=True, upload_to='Employee_CV/%Y/%m/%d', validators=[utilities.pdf_validator.pdf_validator]),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_profile_photo',
            field=models.ImageField(null=True, upload_to=employee_data.media_path_converter.upload_image_path),
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_special_document_photo',
            field=models.ImageField(null=True, upload_to=employee_data.media_path_converter.em_document_path),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='blood_group',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='division',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='post_office',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='thana',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_data.employee_designation'),
        ),
    ]