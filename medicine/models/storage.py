from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=256, verbose_name='药品名称')
    price = models.FloatField(default=0.0, verbose_name='药品单价')
    datetime = models.DateTimeField(max_length=19, verbose_name='入库时间')
    sum = models.IntegerField(default=100, verbose_name='库存')
    exp = models.IntegerField(default=3, verbose_name='保质期/年')

    class Meta:
        verbose_name = '药品'
        verbose_name_plural = '药品'
        ordering = ('id',)

    def __str__(self):
        return self.name
