# Generated by Django 3.2.9 on 2021-12-06 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211206_2012'),
        ('activities', '0002_delete_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]