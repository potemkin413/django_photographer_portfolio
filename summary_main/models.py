from django.db import models

from datetime import date

class About_me(models.Model):
    """Информация обо мне"""
    name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    skill_position = models.CharField("Уровень программирования", max_length=50)
    image = models.ImageField("Аватар", default=None)
    email = models.CharField("Email", default='None', max_length=100, null=True)
    git = models.CharField("Github", default='None', max_length=100, null=True)
    linkedin = models.CharField("Linkedin", default='None', max_length=100, null=True)
    twitter = models.CharField("twitter", default='None', max_length=100, null=True)
    telegram = models.CharField("telegram", default='None', max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"


class Education(models.Model):
    """Образование"""
    title = models.CharField("Название учебного заведения", default="example education", max_length=120)
    description = models.TextField("Описание", default=None, max_length=300)
    year = models.DateTimeField("Период обучения", default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"


class Languages(models.Model):
    """Иностранные языки"""
    name = models.CharField("Иностранный язык", default="English", max_length=100)
    skill = models.CharField("Уровень знания языка", default="Low", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"


class Interests(models.Model):
    """Хобби"""
    name = models.CharField("Хобби", default="Coding", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хобби"
        verbose_name_plural = "Хобби"


class Experiences(models.Model):
    """О своих навыках"""
    title = models.CharField("Название", default="example name experiences", max_length=100)
    description = models.TextField("Описание", default=None)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Опыт разработки"
        verbose_name_plural = "Опыт разработки"


class Projects(models.Model):
    """Выполненные проекты"""
    title = models.CharField("Название", default=None, max_length=50)
    description = models.TextField("Описание", default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Skill_prof(models.Model):
    title = models.CharField("Название", default=None, max_length=100)
    level_skill = models.SmallIntegerField('Уровень', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Умение"
        verbose_name_plural = "Умения"







