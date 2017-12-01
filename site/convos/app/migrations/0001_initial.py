# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-01 19:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.NullBooleanField(default=None)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('interest', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(null=True)),
                ('topic', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('unique_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('food_restrictions', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(choices=[('1', 'M'), ('2', 'F'), ('3', 'O')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_grade', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('convo_grade', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('food_comments', models.TextField(max_length=1000, null=True)),
                ('convo_comments', models.TextField(max_length=1000, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('dinner_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Dinner')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('unique_id', models.CharField(max_length=7, unique=True)),
                ('name', models.CharField(max_length=40)),
                ('food_restrictions', models.CharField(blank=True, max_length=50, null=True)),
                ('netid', models.CharField(max_length=7, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('year', models.CharField(choices=[('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')], max_length=4)),
                ('major', models.CharField(choices=[('1', 'African and African American Studies'), ('2', 'Art History'), ('3', 'Asian and Middel Eastern Studies'), ('4', 'Biology'), ('5', 'Biomedical Engineering'), ('6', 'Biophysics'), ('7', 'Brazilian and Global Portuguese Studies'), ('8', 'Chemistry'), ('9', 'Civil Engineering'), ('10', 'Classical Civilization'), ('11', 'Classical Languages'), ('12', 'Computer Science'), ('13', 'Cultural Anthropology'), ('14', 'Dance'), ('15', 'Earth and Ocean Sciences'), ('16', 'Economics'), ('17', 'Electrical and Computer Engineering'), ('18', 'English'), ('19', 'Environmental Engineering'), ('20', 'Environmental Sciences'), ('21', 'Environmental Sciences and Policy'), ('22', 'Evolutionary Anthropology'), ('23', 'French Studies'), ('24', 'Gender, Sexuality, and Feminist Studies'), ('25', 'German'), ('26', 'Global Cultural Studies'), ('27', 'Global Health'), ('28', 'History'), ('29', 'Interdepartmental Major'), ('30', 'International Comparative Studies'), ('31', 'Italian Studies'), ('32', 'Linguistics'), ('33', 'Mathematics'), ('34', 'Mechanical Engineering'), ('35', 'Medieval and Renaissance Studies'), ('36', 'Music'), ('37', 'Neuroscience'), ('38', 'Philosophy'), ('39', 'Physics'), ('40', 'Political Science'), ('41', 'Program II'), ('42', 'Psychology'), ('43', 'Public Policy Studies'), ('44', 'Religious Studies'), ('45', 'Romance Studies'), ('46', 'Russian'), ('47', 'Slavic and Eurasian Studies'), ('48', 'Sociology'), ('49', 'Spanish, Latin American, and Latino/a Studies'), ('50', 'Statistical Science'), ('51', 'Theater Studies'), ('52', 'Visual Arts'), ('53', 'Visual and Media Studies'), ('54', 'Undecided')], max_length=10)),
                ('pronoun', models.CharField(choices=[('1', 'he/him/his'), ('2', 'she/her/hers'), ('3', 'they/them/theirs'), ('4', 'xe/xem/xyr'), ('5', 'other')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student'),
        ),
        migrations.AddField(
            model_name='dinner',
            name='professor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Professor'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='dinner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Dinner'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student'),
        ),
        migrations.AddField(
            model_name='application',
            name='dinner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Dinner'),
        ),
        migrations.AddField(
            model_name='application',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('username', 'dinner_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('username', 'dinner_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('username', 'dinner_id')]),
        ),
    ]
