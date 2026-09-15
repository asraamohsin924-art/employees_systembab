from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0007_wage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract1000",
            fields=[],
            options={
                "verbose_name": "عقود الألف درجة",
                "verbose_name_plural": "عقود الألف درجة",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("employees.contract",),
        ),
        migrations.CreateModel(
            name="ContractBachelorDiploma",
            fields=[],
            options={
                "verbose_name": "عقود البكالوريوس والدبلوم",
                "verbose_name_plural": "عقود البكالوريوس والدبلوم",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("employees.contract",),
        ),
        migrations.CreateModel(
            name="ContractSecondary",
            fields=[],
            options={
                "verbose_name": "عقود إعدادية فما دون",
                "verbose_name_plural": "عقود إعدادية فما دون",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("employees.contract",),
        ),
    ]
