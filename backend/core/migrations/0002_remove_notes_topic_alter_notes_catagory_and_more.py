# Generated by Django 4.1 on 2023-03-25 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='topic',
        ),
        migrations.AlterField(
            model_name='notes',
            name='catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='catagory', to='core.catagory'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='language', to='core.language'),
        ),
    ]