from django.db import models
from apps.UserInfo.models import UserInfo


class LostFound(models.Model):
    lostFoundId = models.AutoField(primary_key=True, verbose_name='招领id')
    title = models.CharField(max_length=40, default='', verbose_name='标题')
    goodsName = models.CharField(max_length=20, default='', verbose_name='物品名称')
    pickUpTime = models.CharField(max_length=20, default='', verbose_name='捡得时间')
    pickUpPlace = models.CharField(max_length=20, default='', verbose_name='拾得地点')
    contents = models.CharField(max_length=2000, default='', verbose_name='描述说明')
    userObj = models.ForeignKey(UserInfo,  db_column='userObj', on_delete=models.PROTECT, verbose_name='发布人')
    phone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    addTime = models.CharField(max_length=20, default='', verbose_name='发布时间')

    class Meta:
        db_table = 't_LostFound'
        verbose_name = '失物招领信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        lostFound = {
            'lostFoundId': self.lostFoundId,
            'title': self.title,
            'goodsName': self.goodsName,
            'pickUpTime': self.pickUpTime,
            'pickUpPlace': self.pickUpPlace,
            'contents': self.contents,
            'userObj': self.userObj.name,
            'userObjPri': self.userObj.user_name,
            'phone': self.phone,
            'addTime': self.addTime,
        }
        return lostFound

