# Generated by Django 2.0.2 on 2019-07-29 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_auto_20190729_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarryDiffyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('candidate', models.CharField(max_length=200)),
                ('master', models.CharField(max_length=200)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiffyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('db_remark', models.CharField(default='', max_length=100)),
                ('status', models.BooleanField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Case')),
            ],
        ),
        migrations.DeleteModel(
            name='CarryDiffTask',
        ),
        migrations.RemoveField(
            model_name='difftask',
            name='case',
        ),
        migrations.DeleteModel(
            name='DiffTask',
        ),
    ]
