# Generated by Django 4.2.3 on 2023-07-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chess_moves", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="chesspiece", name="piece_type",),
        migrations.RemoveField(model_name="chesspiece", name="position",),
        migrations.AddField(
            model_name="chesspiece",
            name="Bishop",
            field=models.CharField(default=1, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="chesspiece",
            name="Knight",
            field=models.CharField(default=1, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="chesspiece",
            name="Queen",
            field=models.CharField(default=1, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="chesspiece",
            name="Rook",
            field=models.CharField(default=1, max_length=10, null=True),
        ),
    ]