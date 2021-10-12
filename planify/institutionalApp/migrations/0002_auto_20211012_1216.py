# Generated by Django 3.1.7 on 2021-10-12 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutionalApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockbrokerdetails',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorSBDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institutionalbankdetails',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorIBDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institutionalbankdetails',
            name='profileOwner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profileOwnerIBDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institutionaldematdetails',
            name='profileOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profileOwnerIDDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institutionalpersonaldetails',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorIPDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='institutionalpersonaldetails',
            name='profileOwner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profileOwnerIPDI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lookingforprivatecompany',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorLFPCI', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lookingtoinvestdetails',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorLTIDI', to=settings.AUTH_USER_MODEL),
        ),
    ]