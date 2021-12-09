from django.db import models
from django.db.models import signals
from django.dispatch import receiver

# from django.db import data


class Bank (models.Model):  # банк
    # Банк получаеца: 2 поля
    bank_code = models.AutoField("Код банка", primary_key=True)
    bank_name = models.CharField("Наименование банка", max_length=120)

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return f'{self.bank_name}'


class Types_of_Education (models.Model):
    # Виды обучения: 2 поля

    EDUCATION_GRANT = 'Грант'
    EDUCATION_PAID = 'Платная основа'

    EDUCATION_CHOICES = (
        (EDUCATION_GRANT, 'Grand'),
        (EDUCATION_PAID, 'Paid basis')
    )

    education_type_code = models.AutoField(
        "Код вида обучения", primary_key=True)
    education_type_name = models.CharField(
        "Наименование вида обучения", max_length=120, choices=EDUCATION_CHOICES, default=EDUCATION_PAID)

    class Meta:
        verbose_name = 'Вид обучения'
        verbose_name_plural = 'Виды обучения'

    def __str__(self):
        return f'{self.education_type_name}'


class Types_of_Scholarship (models.Model):
    # Виды стипендий: 3 поля

    SCHOLARSHIP_COMMON = 'Обычная'
    SCHOLARSHIP_INCREASED = 'Повышенная'
    SCHOLARSHIP_NOMINAL = 'Именная'
    SCHOLARSHIP_SOCIAL = 'Социальная'

    SCHOLARSHIP_CHOICES = (
        (SCHOLARSHIP_COMMON, 'common'),
        (SCHOLARSHIP_INCREASED, 'increased'),
        (SCHOLARSHIP_NOMINAL, 'nominal'),
        (SCHOLARSHIP_SOCIAL, 'social')
    )

    scholarship_type_code = models.AutoField(
        "Код вида стипендии", primary_key=True)
    scholarship_type_name = models.CharField(
        "Код вида стипендии", max_length=25, choices=SCHOLARSHIP_CHOICES, default=SCHOLARSHIP_COMMON)
    amount_of_money = models.PositiveIntegerField(
        "Сумма выплачиваемой стипендии, ₸",)

    class Meta:
        verbose_name = 'Вид стипендии'
        verbose_name_plural = 'Виды стипендий'

    def __str__(self):
        return f'{self.scholarship_type_name}'


class Staff (models.Model):
    # Сотрудники: 2 поля
    сurator_code = models.AutoField(
        "Код сотрудника", primary_key=True)     # код сотрудника
    curator_name = models.CharField("Имя сотрудника", max_length=200)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.curator_name}'


class Faculty (models.Model):
    # ФАКУЛЬТЕТ: 3 поля
    faculty_code = models.AutoField("Код факультета", primary_key=True)
    faculty_name = models.CharField("Наименование факультета", max_length=120)
    # код сотр. деканата ОТНОШЕНИЕ 1:1 с Staff
    deanery_employee_code = models.OneToOneField(
        Staff, verbose_name="Декан факультета", null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return f'{self.faculty_name}'


class Department (models.Model):
    # Кафедры: 4 поля
    department_code = models.AutoField("Код кафедры", primary_key=True)
    department_name = models.CharField("Наименование кафедры", max_length=120)
    # FOREIGN KEY ОТНОШЕНИЕ 1:M с Faculty
    faculty_code = models.ForeignKey(
        Faculty, verbose_name="Код факультета", on_delete=models.CASCADE)
    # код сотр. зав. каф. ОТНОШЕНИЕ 1:1 с Staff
    department_head_code = models.OneToOneField(
        Staff, verbose_name="Заведующий кафедрой", null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return f'{self.department_name}'


class Group (models.Model):
    # Группы: 5 поля
    group_code = models.AutoField("Код группы", primary_key=True)
    group_name = models.CharField("Наименование группы", max_length=120)
    # FOREIGN KEY ОТНОШЕНИЕ 1:M с Department
    issuing_department_code = models.ForeignKey(
        Department, verbose_name="Код выпускающей кафедры", on_delete=models.CASCADE)
    сurator_code = models.OneToOneField(Staff, verbose_name="Код куратора группы", null=True,
                                        blank=True, on_delete=models.PROTECT)        # код куратора ОТНОШЕНИЕ 1:1 с Staff

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.group_name}'


class Student (models.Model):
    # Студенты: 6 поля
    student_code = models.AutoField(
        "Код студента", primary_key=True)     # код студента
    student_name = models.CharField("Имя студента", max_length=200)
    # FOREIGN KEY ОТНОШЕНИЕ 1:M с Group
    group_code = models.ForeignKey(
        Group, verbose_name="Группа", on_delete=models.CASCADE)
    # FOREIGN KEY ОТНОШЕНИЕ 1:M с Types_of_Education
    education_type_code = models.ForeignKey(
        Types_of_Education, verbose_name="Код вида обучения", on_delete=models.CASCADE)
    personal_reckoning_number = models.IntegerField("Номер лицевого счета")
    bank_code = models.ForeignKey(Bank, verbose_name="Код банка", on_delete=models.CASCADE,
                                  null=True, blank=True)     # FOREIGN KEY ОТНОШЕНИЕ 1:M с Bank

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f'{self.student_name}'


class Accrual (models.Model):
    # Начисления: 3 поля
    student_code = models.ForeignKey(
        Student, verbose_name="Имя студента", on_delete=models.CASCADE)
    date_of_scholarship_accrual = models.DateField(
        "Дата начисления стипендии", null=True, blank=True)                    # дата начисления стипендии
    amount_of_money = models.PositiveIntegerField(
        "Сумма начисления", null=True, blank=True)  # сумма

    class Meta:
        verbose_name = 'Начисление'
        verbose_name_plural = 'Начисления'


class Scholarship_Fund (models.Model):
    # Стипендиальный фонд: 2 поля
    faculty_code = models.OneToOneField(Faculty, verbose_name="Код факультета",
                                        on_delete=models.CASCADE, primary_key=True)  # FOREIGN KEY ОТНОШЕНИЕ 1:1 с Faculty
    scholarship_amount = models.PositiveIntegerField(
        "Сумма стипендий", null=True, blank=True)         # сумма стипендий

    class Meta:
        verbose_name = 'Стипендиальный фонд'
        verbose_name_plural = 'Стипендиальные фонды'

    def save(self, **kwargs):
        total = 0
        students = Accrual.objects.filter(
            student_code__group_code__issuing_department_code__faculty_code=self.faculty_code)
        for stud in students:
            total += stud.amount_of_money
        self.scholarship_amount = total
        super().save(**kwargs)

# сигнал после сохранения нового объекта начисления


def update_fund(sender, instance, created, **kwargs):
    fund = Scholarship_Fund.objects.get(
        faculty_code=instance.student_code.group_code.issuing_department_code.faculty_code)
    fund.save()


signals.post_save.connect(receiver=update_fund, sender=Accrual)


class Fellow (models.Model):
    # Стипендиаты: 4 поля
    student_code = models.OneToOneField(
        Student, verbose_name="Код студента", on_delete=models.CASCADE)
    scholarship_type_code = models.ForeignKey(
        Types_of_Scholarship, verbose_name="Вид стипендии", on_delete=models.CASCADE, null=True, blank=True)
    beginning_of_the_accrual_period = models.DateField(
        "Начало периода начисления", null=True, blank=True)
    ending_of_the_accrual_period = models.DateField(
        "Конец периода начисления", null=True, blank=True)

    class Meta:
        verbose_name = 'Стипендиат'
        verbose_name_plural = 'Стипендиаты'

    def __str__(self) -> str:
        return f'{self.student_code}'
