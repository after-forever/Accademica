from django.db import models

class Collection(models.Model):
    isbn = models.CharField(verbose_name="ISBN", max_length=13, null=True)
    title = models.CharField(verbose_name="書名", max_length=256)
    price = models.IntegerField(verbose_name="価格", default=0)
    author = models.CharField(verbose_name="著者", max_length=256, null=True)
    publisher = models.CharField(verbose_name="出版社", max_length=256, null=True)
    publishing_date = models.DateField(verbose_name="発売日", null=True)
    created_at = models.DateTimeField(verbose_name="登録日", auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Collection'

    def __str__(self):
         return self.title