from django.db import models


class Notice(models.Model):
    noticeId = models.AutoField(primary_key=True, verbose_name='通知id')
    title = models.CharField(max_length=50, default='', verbose_name='标题')
    content = models.CharField(max_length=2000, default='', verbose_name='内容')
    addTime = models.CharField(max_length=20, default='', verbose_name='发布时间')

    class Meta:
        db_table = 't_Notice'
        verbose_name = '站内通知信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        notice = {
            'noticeId': self.noticeId,
            'title': self.title,
            'content': self.content,
            'addTime': self.addTime,
        }
        return notice

