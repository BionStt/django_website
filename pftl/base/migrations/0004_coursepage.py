# Generated by Django 2.2.8 on 2019-12-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_bookspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.BasePage')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.basepage',),
        ),
    ]