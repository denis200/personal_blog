# Generated by Django 4.0.4 on 2022-05-15 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_created'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollowing',
            name='user_id',
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='following', to='blog.blog'),
            preserve_default=False,
        ),
    ]
