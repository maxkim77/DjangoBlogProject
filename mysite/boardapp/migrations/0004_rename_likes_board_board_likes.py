# Generated by Django 4.2.6 on 2023-10-31 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_board_likes_board_view_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='likes',
            new_name='board_likes',
        ),
    ]
