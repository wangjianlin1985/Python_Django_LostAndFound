from django.db import models
from apps.UserInfo.models import UserInfo


class LookingFor(models.Model):
    lookingForId = models.AutoField(primary_key=True, verbose_name='寻物id')
    title = models.CharField(max_length=30, default='', verbose_name='标题')
    goodsName = models.CharField(max_length=40, default='', verbose_name='丢失物品')
    goodsPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='物品照片')
    lostTime = models.CharField(max_length=20, default='', verbose_name='丢失时间')
    lostPlace = models.CharField(max_length=20, default='', verbose_name='丢失地点')
    goodDesc = models.CharField(max_length=500, default='', verbose_name='物品描述')
    reward = models.CharField(max_length=40, default='', verbose_name='报酬')
    telephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    userObj = models.ForeignKey(UserInfo,  db_column='userObj', on_delete=models.PROTECT, verbose_name='发布用户')
    addTime = models.CharField(max_length=20, default='', verbose_name='发布时间')

    class Meta:
        db_table = 't_LookingFor'
        verbose_name = '寻物启事信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        lookingFor = {
            'lookingForId': self.lookingForId,
            'title': self.title,
            'goodsName': self.goodsName,
            'goodsPhoto': self.goodsPhoto.url,
            'lostTime': self.lostTime,
            'lostPlace': self.lostPlace,
            'goodDesc': self.goodDesc,
            'reward': self.reward,
            'telephone': self.telephone,
            'userObj': self.userObj.name,
            'userObjPri': self.userObj.user_name,
            'addTime': self.addTime,
        }
        return lookingFor

