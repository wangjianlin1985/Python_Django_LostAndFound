from django.db import models
from apps.LostFound.models import LostFound


class Praise(models.Model):
    praiseId = models.AutoField(primary_key=True, verbose_name='表扬id')
    lostFoundObj = models.ForeignKey(LostFound,  db_column='lostFoundObj', on_delete=models.PROTECT, verbose_name='招领信息')
    title = models.CharField(max_length=40, default='', verbose_name='标题')
    contents = models.CharField(max_length=300, default='', verbose_name='表扬内容')
    addTime = models.CharField(max_length=20, default='', verbose_name='表扬时间')

    class Meta:
        db_table = 't_Praise'
        verbose_name = '表扬信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        praise = {
            'praiseId': self.praiseId,
            'lostFoundObj': self.lostFoundObj.title,
            'lostFoundObjPri': self.lostFoundObj.lostFoundId,
            'title': self.title,
            'contents': self.contents,
            'addTime': self.addTime,
        }
        return praise

