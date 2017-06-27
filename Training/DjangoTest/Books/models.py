#encoding=utf-8
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    class Meta:
        # class Meta，内嵌于 Publisher 这个类的定义中（如果 class Publisher 是顶格的，那么 class Meta 在它之下要缩进4个空格－－按 Python 的传统 ）。
        # 你可以在任意一个 模型 类中使用 Meta 类，来设置一些与特定模型相关的选项。 在 附录B 中有 Meta 中所有可选项的完整参考，现在，我们关注 ordering 这个选项就够了。
        # 如果你设置了这个选项，那么除非你检索时特意额外地使用了 order_by()，否则，当你使用 Django 的数据库 API 去检索时，Publisher对象的相关返回值默认地都会按 name 字段排序。
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
# 我们并没有显式地为这些模型定义任何主键。 除非你单独指明，否则Django会自动为每个模型生成一个自增长的整数主键字段每个Django模型都要求有单独的主键。id
