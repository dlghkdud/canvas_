# Generated by Django 3.2.23 on 2023-11-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palette', '0008_alter_comment_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadedFile', models.FileField(upload_to='result/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
