# Generated by Django 2.2.5 on 2020-05-27 15:36

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名')),
                ('desc', models.TextField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目')),
            ],
            options={
                'verbose_name': '宣传品牌',
                'verbose_name_plural': '宣传品牌',
                'db_table': 'goods_goodsbrand',
            },
        ),
    ]
