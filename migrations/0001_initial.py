# Generated by Django 2.1.7 on 2019-04-28 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=100, verbose_name='年级')),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge1', models.CharField(max_length=50, verbose_name='一级知识点')),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge2', models.CharField(max_length=50, verbose_name='二级知识点')),
                ('knowledge1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Knowledge1')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='试卷名称')),
                ('points', models.IntegerField(verbose_name='总分')),
                ('user_id', models.IntegerField(default=0, verbose_name='录人员')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='Paper_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='题目内容')),
                ('types', models.CharField(choices=[('选择题', '选择题'), ('判断题', '判断题'), ('填空题', '填空题'), ('解答题', '解答题')], max_length=30, verbose_name='题目类型')),
                ('option1', models.CharField(blank=True, max_length=50, null=True, verbose_name='A')),
                ('option2', models.CharField(blank=True, max_length=50, null=True, verbose_name='B')),
                ('option3', models.CharField(blank=True, max_length=50, null=True, verbose_name='C')),
                ('option4', models.CharField(blank=True, max_length=50, null=True, verbose_name='D')),
                ('difficult', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='难度系数')),
                ('answer', models.CharField(max_length=300, verbose_name='答案')),
                ('photo', models.CharField(blank=True, max_length=50, null=True, verbose_name='图片')),
                ('formula', models.CharField(blank=True, max_length=50, null=True, verbose_name='公式')),
                ('user_id', models.IntegerField(default=0, verbose_name='录人员')),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Grade')),
                ('knowledge1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Knowledge1')),
                ('knowledge2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Knowledge2')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=50, verbose_name='学校')),
                ('school_info', models.CharField(max_length=50, verbose_name='学校性质')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='科目')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('email', models.EmailField(max_length=32, verbose_name='email')),
                ('role', models.CharField(max_length=8, verbose_name='身份')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.School'),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Subject'),
        ),
        migrations.AddField(
            model_name='paper_detail',
            name='question_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Question'),
        ),
        migrations.AddField(
            model_name='paper',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.School'),
        ),
        migrations.AddField(
            model_name='paper',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Subject'),
        ),
        migrations.AddField(
            model_name='knowledge1',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_library.Subject'),
        ),
    ]