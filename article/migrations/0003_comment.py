# Generated by Django 5.1.6 on 2025-02-21 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_article_article_image_alter_article_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "comment_author",
                    models.CharField(max_length=50, verbose_name="İsim"),
                ),
                (
                    "comment_content",
                    models.CharField(max_length=200, verbose_name="Yorum"),
                ),
                ("comment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Comments",
                        to="article.article",
                        verbose_name="Makale",
                    ),
                ),
            ],
        ),
    ]
