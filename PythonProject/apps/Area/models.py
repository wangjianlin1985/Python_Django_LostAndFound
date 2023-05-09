from django.db import models


class Area(models.Model):
    areaId = models.AutoField(primary_key=True, verbose_name='区域id')
    areaName = models.CharField(max_length=20, default='', verbose_name='区域名称')

    class Meta:
        db_table = 't_Area'
        verbose_name = '区域信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        area = {
            'areaId': self.areaId,
            'areaName': self.areaName,
        }
        return area

