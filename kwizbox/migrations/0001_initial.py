# Generated by Django 4.0.6 on 2022-07-30 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoOfWeeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizzId', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=255)),
                ('twitterHandle', models.CharField(max_length=255, null=True)),
                ('walletAddress', models.CharField(max_length=255)),
                ('whoReferedMe', models.CharField(blank=True, max_length=255, null=True)),
                ('myRefrealCode', models.CharField(blank=True, max_length=255, null=True)),
                ('isKycVerified', models.CharField(blank=True, default='False', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('weekId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwizbox.noofweeks')),
            ],
        ),
        migrations.CreateModel(
            name='KYCData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('IdNumber', models.CharField(max_length=255)),
                ('documentFile', models.FileField(upload_to='Files/')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwizbox.user')),
            ],
        ),
        migrations.CreateModel(
            name='courseCompleted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isWeek1Completed', models.BooleanField(default=False)),
                ('isWeek2Completed', models.BooleanField(default=False)),
                ('isWeek3Completed', models.BooleanField(default=False)),
                ('isWeek4Completed', models.BooleanField(default=False)),
                ('score1', models.CharField(blank=True, max_length=200, null=True)),
                ('score2', models.CharField(blank=True, max_length=200, null=True)),
                ('score3', models.CharField(blank=True, max_length=200, null=True)),
                ('score4', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kwizbox.user')),
            ],
        ),
    ]
