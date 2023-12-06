# Generated by Django 4.2.7 on 2023-12-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CandY_Server", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TB_FITBIT",
            fields=[
                (
                    "experiment_idx",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("session_id", models.CharField(max_length=150)),
                ("user_id", models.CharField(max_length=30)),
                ("datetime", models.DateTimeField()),
                ("hr", models.FloatField(blank=True, null=True)),
                ("hrv", models.FloatField(blank=True, null=True)),
                ("coherence", models.FloatField(blank=True, null=True)),
                ("body_movement", models.IntegerField(blank=True, null=True)),
                ("deep_sleep_minutes", models.IntegerField(blank=True, null=True)),
                ("eda", models.FloatField(blank=True, null=True)),
                ("wrist_temperature", models.FloatField(blank=True, null=True)),
                ("concentration_score", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "TB_FITBIT",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TB_MEMBER",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("user_pw", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "TB_MEMBER",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="TB_SESSION_RESULT",
            fields=[
                (
                    "session_id",
                    models.CharField(max_length=150, primary_key=True, serialize=False),
                ),
                ("user_id", models.CharField(max_length=30)),
                (
                    "session_place",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("session_start_time", models.DateTimeField()),
                ("session_end_time", models.DateTimeField()),
                ("concentration_score_avg", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "TB_SESSION_RESULT",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="TbFitbit",
        ),
        migrations.DeleteModel(
            name="TbMember",
        ),
        migrations.DeleteModel(
            name="TbSessionResult",
        ),
    ]