# Generated by Django 3.2 on 2021-04-14 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210404_0716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accrual',
            options={'verbose_name': 'Начисление', 'verbose_name_plural': 'Начисления'},
        ),
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name': 'Банк', 'verbose_name_plural': 'Банки'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Кафедра', 'verbose_name_plural': 'Кафедры'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Факультет', 'verbose_name_plural': 'Факультеты'},
        ),
        migrations.AlterModelOptions(
            name='fellow',
            options={'verbose_name': 'Стипендиат', 'verbose_name_plural': 'Стипендиаты'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='scholarship_fund',
            options={'verbose_name': 'Стипендиальный фонд', 'verbose_name_plural': 'Стипендиальные фонды'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='types_of_education',
            options={'verbose_name': 'Вид обучения', 'verbose_name_plural': 'Виды обучения'},
        ),
        migrations.AlterModelOptions(
            name='types_of_scholarship',
            options={'verbose_name': 'Вид стипендии', 'verbose_name_plural': 'Виды стипендий'},
        ),
        migrations.AlterField(
            model_name='department',
            name='department_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='faculty_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='сurator_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types_of_education',
            name='education_type_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types_of_education',
            name='education_type_name',
            field=models.CharField(choices=[('Grand', 'Грант'), ('Paid basis', 'Платная основа')], max_length=120),
        ),
        migrations.AlterField(
            model_name='types_of_scholarship',
            name='amount_of_money',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='types_of_scholarship',
            name='scholarship_type_name',
            field=models.CharField(choices=[('common', 'Обычная'), ('increased', 'Повышенная'), ('nominal', 'Именная'), ('social', 'Социальная')], max_length=25),
        ),
    ]
