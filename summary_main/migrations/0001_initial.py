# Generated by Django 3.0.8 on 2020-07-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('skill_position', models.CharField(max_length=50, verbose_name='Уровень программирования')),
                ('image', models.ImageField(default=None, upload_to='', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
        migrations.CreateModel(
            name='Carer_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default=None, max_length=1000, verbose_name='Опыт работы')),
            ],
            options={
                'verbose_name': 'Опыт',
                'verbose_name_plural': 'Опыт',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git', models.CharField(default=None, max_length=100, verbose_name='Github')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='example education', max_length=120, verbose_name='Название учебного заведения')),
                ('description', models.TextField(default=None, max_length=300, verbose_name='Описание')),
                ('year', models.DateTimeField(default=None, verbose_name='Период обучения')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='example name experiences', max_length=50, verbose_name='Название')),
                ('description', models.TextField(default=None, verbose_name='Описание')),
                ('post_time', models.DateTimeField(default=None, verbose_name='Время поста')),
            ],
            options={
                'verbose_name': 'Опыт разработки',
                'verbose_name_plural': 'Опыт разработки',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Coding', max_length=100, verbose_name='Хобби')),
            ],
            options={
                'verbose_name': 'Хобби',
                'verbose_name_plural': 'Хобби',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='English', max_length=100, verbose_name='Иностранный язык')),
                ('skill', models.CharField(default='Low', max_length=100, verbose_name='Уровень знания языка')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=50, verbose_name='Название')),
                ('description', models.TextField(default=None, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Skill_prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='Название')),
                ('level_skill', models.SmallIntegerField(default=0, verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Умение',
                'verbose_name_plural': 'Умения',
            },
        ),
    ]
