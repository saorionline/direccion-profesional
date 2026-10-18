from django.db import migrations

TITLE = "Storytelling with Data: A Data Visualization Guide for Business Professionals"
AUTHORS = "Cole Nussbaumer Knaflic"


def add_reference(apps, schema_editor):
    Reference = apps.get_model("portfolio", "Reference")
    Reference.objects.get_or_create(
        title=TITLE,
        authors=AUTHORS,
        defaults={"year": 2015, "source": "Wiley", "published": True},
    )


def remove_reference(apps, schema_editor):
    Reference = apps.get_model("portfolio", "Reference")
    Reference.objects.filter(title=TITLE, authors=AUTHORS).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_article_reference"),
    ]

    operations = [
        migrations.RunPython(add_reference, remove_reference),
    ]
