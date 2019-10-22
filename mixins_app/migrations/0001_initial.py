# Generated by Django 2.2.4 on 2019-10-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentname', models.CharField(default=False, max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Atendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statues', models.CharField(choices=[('Present', 'Presentt'), ('Absent', 'Absent')], default=False, max_length=1)),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixins_app.Student')),
                ('teachename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mixins_app.Teacher')),
            ],
        ),
    ]
