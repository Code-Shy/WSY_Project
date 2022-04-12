from django.db import models

class Income(models.Model):
    sum = models.FloatField(default=0.0, verbose_name="金额/(元)")
    type = models.CharField(max_length=64, verbose_name="类型")
    datatime = models.DateTimeField(max_length=19, verbose_name="时间")
    purpose = models.CharField(max_length=256, verbose_name="用途")
    remark = models.CharField(max_length=256, verbose_name="备注")

    class Meta:
        verbose_name = '收支管理'
        verbose_name_plural = '收支管理'

    def __str__(self):
        return  self.type