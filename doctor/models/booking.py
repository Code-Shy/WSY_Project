from django.db import models


class Booking(models.Model):
    time = models.DateTimeField(max_length=19, verbose_name='时间')
    exp = models.DateTimeField(max_length=19, verbose_name='过期时间')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='用户')

    class Meta:
        verbose_name = '预约信息'
        verbose_name_plural = '预约信息'

    def __str__(self):
        return  str(self.id)
