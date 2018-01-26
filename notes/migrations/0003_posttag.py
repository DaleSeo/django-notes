# Generated by Django 2.0.1 on 2018-01-26 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=45)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.Post')),
            ],
        ),
    ]