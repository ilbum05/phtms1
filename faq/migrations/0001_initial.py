# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumchoicefield.fields
import faq.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('buz_no', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='VAT No.')),
                ('buz_type', enumchoicefield.fields.EnumChoiceField(enum_class=faq.models.Enum_Buztype, max_length=1)),
                ('zipcode', models.CharField(max_length=5, verbose_name='Zip-Code.')),
                ('point', models.SmallIntegerField(verbose_name='Point')),
                ('cdate', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('mdate', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_kind', enumchoicefield.fields.EnumChoiceField(enum_class=faq.models.Enum_Kind, max_length=2)),
                ('owner', models.CharField(max_length=20, null=True, verbose_name='Owner.')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject.')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('attach', models.FileField(blank=True, upload_to='uploads/faq/%Y/%m/%d/', verbose_name='Attachment.')),
                ('passno', models.CharField(help_text='Required. 4 digits Only.', max_length=4, null=True, verbose_name='Password.')),
                ('cdate', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('mdate', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('buz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.Company')),
            ],
            options={
                'verbose_name_plural': 'faqs',
                'db_table': 'faq',
                'ordering': ['-mdate'],
            },
        ),
    ]
