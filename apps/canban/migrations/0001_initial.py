# Generated by Django 4.2 on 2023-05-02 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Board title')),
                ('title_uz', models.CharField(max_length=256, null=True, unique=True, verbose_name='Board title')),
                ('title_en', models.CharField(max_length=256, null=True, unique=True, verbose_name='Board title')),
                ('title_ru', models.CharField(max_length=256, null=True, unique=True, verbose_name='Board title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Board',
                'verbose_name_plural': 'Boards',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=64, null=True, unique=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=64, null=True, unique=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=64, null=True, unique=True, verbose_name='Title')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='canban.board', verbose_name='Board')),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Columns',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='canban.column', verbose_name='Column')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='Title')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='canban.task', verbose_name='Subtask')),
            ],
            options={
                'verbose_name': 'Subtask',
                'verbose_name_plural': 'Subtasks',
            },
        ),
    ]