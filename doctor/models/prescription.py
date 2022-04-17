from django.db import models


class Prescription(models.Model):
    time = models.DateTimeField(max_length=19, verbose_name='时间')
    content = models.CharField(max_length=256, verbose_name='内容')
    doctor = models.CharField(max_length=256, verbose_name='主治医师')
    customer = models.ForeignKey('Customer',  on_delete=models.CASCADE, default='',verbose_name='用户')

    class Meta:
        verbose_name = '处方信息'
        verbose_name_plural = '处方信息'

    def __str__(self):
        return str(self.id)