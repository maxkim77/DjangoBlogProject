# Generated by Django 4.2.6 on 2023-10-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_notice',
            field=models.BooleanField(default=False, verbose_name='공지사항 여부'),
        ),
    ]
