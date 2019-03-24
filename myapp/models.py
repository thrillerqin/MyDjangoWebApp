from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    '''用户学习的主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text

class Entry(models.Model):
    '''某个主题的具体知识'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''返回模型的字符串表示'''
        return self.text[:50]


class BdnkDeviceIdInfo(models.Model):
    '''用户设备信息（外键User）,device_id_info'''
    bdnk_device_id_info = models.ForeignKey(User, on_delete=models.CASCADE)
    sn = models.CharField(max_length=20, default='')
    imei = models.CharField(max_length=20, default='')  #, primary_key=True)
    ccid = models.CharField(max_length=20, default='')
    imsi = models.CharField(max_length=20, default='')
    version = models.CharField(max_length=20, default='')
    product_type = models.CharField(max_length=20, default='Z001')

    def __str__(self):
        return self.imei

class BdnkDeviceStatus(models.Model):
    '''用户设备状态信息'''
    bdnk_device_status = models.ForeignKey(User, on_delete=models.CASCADE)
    sn = models.CharField(max_length=20,default='')
    imei = models.CharField(max_length=20,default='')
    interval = models.CharField(max_length=20, default='')
    led = models.CharField(max_length=20, default = '')
    enable_shut_off_by_pwrkey = models.CharField(max_length=20, default = '')
    run_status = models.CharField(max_length=20, default = '')
    phone_number = models.CharField(max_length=64, default = '13800000000')

    def __str__(self):
        return 'bdnk device status'

class BdnkData(models.Model):
    '''北斗纽扣接收数据的'''
    # bdnk_device_data_record = models.ForeignKey(BdnkDeviceIdInfo, on_delete=models.CASCADE)
    # bdnk_device_data_record = models.ForeignKey(User, on_delete=models.CASCADE)
    # bdnk_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sn = models.CharField(max_length=20,default='')
    imei = models.CharField(max_length=20,default='')
    lat = models.CharField(max_length=20,default='')
    long = models.CharField(max_length=20,default='')
    altitude = models.CharField(max_length=20,default='')
    locate_mode = models.CharField(max_length=20,default='')
    bat = models.CharField(max_length=20,default='')
    si = models.CharField(max_length=20,default='')
    elapse = models.CharField(max_length=30,default='')
    time = models.CharField(max_length=30,default='')

    def __str__(self):
        return 'bdnk device data record'

