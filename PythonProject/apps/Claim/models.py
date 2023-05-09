from django.db import models
from apps.LostFound.models import LostFound


class Claim(models.Model):
    claimId = models.AutoField(primary_key=True, verbose_name='认领id')
    lostFoundObj = models.ForeignKey(LostFound,  db_column='lostFoundObj', on_delete=models.PROTECT, verbose_name='招领信息')
    personName = models.CharField(max_length=20, default='', verbose_name='认领人')
    claimTime = models.CharField(max_length=20, default='', verbose_name='认领时间')
    contents = models.CharField(max_length=500, default='', verbose_name='描述说明')
    addTime = models.CharField(max_length=20, default='', verbose_name='发布时间')

    class Meta:
        db_table = 't_Claim'
        verbose_name = '认领信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        claim = {
            'claimId': self.claimId,
            'lostFoundObj': self.lostFoundObj.title,
            'lostFoundObjPri': self.lostFoundObj.lostFoundId,
            'personName': self.personName,
            'claimTime': self.claimTime,
            'contents': self.contents,
            'addTime': self.addTime,
        }
        return claim

