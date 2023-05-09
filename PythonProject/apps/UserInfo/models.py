from django.db import models
from apps.Area.models import Area


class UserInfo(models.Model):
    user_name = models.CharField(max_length=20, default='', primary_key=True, verbose_name='用户名')
    password = models.CharField(max_length=20, default='', verbose_name='登录密码')
    areaObj = models.ForeignKey(Area,  db_column='areaObj', on_delete=models.PROTECT, verbose_name='所在区域')
    name = models.CharField(max_length=20, default='', verbose_name='姓名')
    sex = models.CharField(max_length=4, default='', verbose_name='性别')
    userPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='用户照片')
    birthday = models.CharField(max_length=20, default='', verbose_name='出生日期')
    telephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    address = models.CharField(max_length=50, default='', verbose_name='家庭地址')

    class Meta:
        db_table = 't_UserInfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        userInfo = {
            'user_name': self.user_name,
            'password': self.password,
            'areaObj': self.areaObj.areaName,
            'areaObjPri': self.areaObj.areaId,
            'name': self.name,
            'sex': self.sex,
            'userPhoto': self.userPhoto.url,
            'birthday': self.birthday,
            'telephone': self.telephone,
            'address': self.address,
        }
        return userInfo

