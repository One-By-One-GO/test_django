from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户ID')
    username = models.CharField(max_length=100, verbose_name='用户名')

    class Meta:
        db_table = 'User'


class Meeting(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='会议室id')
    meeting_name = models.CharField(max_length=100, verbose_name='会议室名称')
    create_userid = models.IntegerField(verbose_name='创建用户id')
    update_userid = models.IntegerField(verbose_name='修改用户id')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    is_delete = models.IntegerField(default=False, verbose_name='删除（是1/否0）')

    class Meta:
        db_table = 'Meeting'
        unique_together = ('meeting_name', 'is_delete')


class Reserve(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='预定ID')
    reserve_userid = models.IntegerField(verbose_name='预定用户id')
    meeting_id = models.ForeignKey('Meeting', on_delete=models.CASCADE,
                                   related_name='meeting_id', verbose_name='会议室id')
    reserve_time = models.DateField(verbose_name='预定时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'Reserve'
        unique_together = ('meeting_id', 'reserve_time')
