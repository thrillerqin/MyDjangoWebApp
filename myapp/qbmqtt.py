import paho.mqtt.client as mqtt
import time

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.http import HttpResponseRedirect,HttpResponse

from .models import Topic,BdnkData,BdnkDeviceIdInfo,BdnkDeviceStatus
from .forms import TopicForm,EntryForm,BdnkDataForm,BdnkDeviceIdInfoForm

global ZJSD_BDNK_MQTT_TOPIC_DATA

HOST = "www.ry9r4e4.mqtt.iot.bj.baidubce.com"
PORT = 1883
ZJSD_BDNK_MQTT_TOPIC_DATA = 'this  is a trap!!!!!!!!!!!!!!!!!!!!!!!!'
ZJSD_BDNK_MQTT_TOPIC_REGISTER = '/zjsd/device/register'


def client_loop():
    client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.username_pw_set("ry9r4e4/qinbao", "B1LI6gzQp+2j7NtcpTVYg4+6I8lbKTL4ncXLndqFY4Q=")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    # client.loop_forever()
    client.loop_start()

def on_connect(client, userdata, flags, rc):
    # print('1111111111111111111111111111111111111111111111111111')
    # msgs = BdnkDeviceStatus.objects.all()
    # print('数据库BdnkDeviceStatus的总行个数:')
    # print(msgs.count())  # 数据库的行个数
    #
    # msgs = BdnkDeviceStatus.objects.filter(imei__contains='867186032871013')
    # print('数据库某imei的行个数:')
    # print(msgs.count())  # 数据库的行个数
    # # print(msgs.objects.all())
    #
    # # 返回的 QuerySet 对象中，不包含 imei='xxx' 的 model 对象
    # msgs = BdnkDeviceStatus.objects.exclude(imei='867186032871013')
    # print('数据库不包含某imei的行个数:')
    # print(msgs.count())  # 数据库的行个数
    # # print(msgs.objects.all())
    # msgs.delete()
    #
    # msgs = BdnkDeviceStatus.objects.all()
    # print('数据库的行个数:')
    # print(msgs.count())  # 数据库的行个数
    #
    # # print(type(msgs))
    # # qblist = list(msgs)
    # # print(qblist)
    # # for item in msgs:
    # #     print(item.sn)
    # # msgs = BdnkDeviceStatus.objects.filter(sn="1234")
    # # print(msgs)
    # # # msgs = BdnkDeviceStatus.objects.filter(imei__contains='867186032871013')
    # # # print(msgs.objects.all())
    # # print(type(msgs))
    # while(1):
    #     pass
    print("Connected with result code "+str(rc))
    print('subscribe topic: ' + ZJSD_BDNK_MQTT_TOPIC_REGISTER)
    client.subscribe(ZJSD_BDNK_MQTT_TOPIC_REGISTER)

def on_message(client, userdata, msg):
    global ZJSD_BDNK_MQTT_TOPIC_DATA
    # print(msg.topic+" "+msg.payload.decode("utf-8"))
    if (msg.topic == ZJSD_BDNK_MQTT_TOPIC_REGISTER):    # 注册主题
        print('received register message')
        qb_dict = eval(msg.payload.decode("utf-8"))
        # qb_dict = {'product_type': 'Z001',
        #            'ccid': '89860402101890678477',
        #            'version': '18041801',
        #            'sn': '123456789',
        #            'imsi': 'x',
        #             'imei': '867186032871013'}
        my_mqtt_topic = '/'
        my_mqtt_topic = my_mqtt_topic.join([qb_dict['product_type'], qb_dict['imei'], qb_dict['sn']])
        my_mqtt_topic = '/' + my_mqtt_topic + '/data'
        print(my_mqtt_topic)
        print('subscribe topic: ' + my_mqtt_topic)
        client.subscribe(my_mqtt_topic)
        ZJSD_BDNK_MQTT_TOPIC_DATA = my_mqtt_topic

        print('qb_dict:')
        print(qb_dict)
        print(type(qb_dict))
        # ['sn', 'imei', 'ccid', 'imsi', 'version', 'product_type']
        # del qb_dict['phone_number']
        # del qb_dict['enable_shut_off_by_pwrkey']
        # del qb_dict['fota_addr']
        # fields = ['sn', 'imei', 'ccid', 'imsi', 'version', 'product_type']
        # qb_dict['imsi'] = 'xyz'
        # print('popped qb_dict:')
        # print(qb_dict)
        # print(type(qb_dict))
        # qb_dict = {'imei': '12345'}
        # print('new qb_dict:')
        # print(qb_dict)
        # print(type(qb_dict))
        # form = BdnkDeviceIdInfoForm(qb_dict)
        # if form.is_valid():
        #     print('saving BdnkDeviceIdInfoForm...')
        #     form.save()

        # 返回的 QuerySet 对象中，不包含 imei='xxx' 的 model 对象
        qbqueryset = BdnkDeviceIdInfo.objects.filter(imei__contains=qb_dict['imei'])
        print('数据库包含某imei的行个数:')
        print(qbqueryset.count())  # 数据库的行个数
        if ((qbqueryset.count() > 1) or (qbqueryset.count() == 0)):
            qbqueryset.delete()
            # 在数据库BdnkDeviceIdInfo新建一行
            BdnkDeviceIdInfo.objects.create(sn=qb_dict['sn'],
                                            imei=qb_dict['imei'],
                                            ccid=qb_dict['ccid'],
                                            imsi=qb_dict['imsi'],
                                            version=qb_dict['version'],
                                            product_type=qb_dict['product_type'])
            print('saving BdnkDeviceIdInfo...')
        else:
            print('update BdnkDeviceIdInfo...')
            qbqueryset.update(version=qb_dict['version'])   # 跟新版本信息
    elif(msg.topic == ZJSD_BDNK_MQTT_TOPIC_DATA):   # 接收数据的主题
        print('ZJSD_BDNK_MQTT_TOPIC_DATA: ')
        print(ZJSD_BDNK_MQTT_TOPIC_DATA)
        print(msg.topic + " " + msg.payload.decode("utf-8"))
        # qb_dict = {"lat": "40.823532",
        #            "long": "116.284368",
        #            "locate_mode": "LBS",
        #            "bat": "84",
        #            "si": "24",
        #            "elapse": "71493",
        #            "time": "2019-03-21 13:50:41",
        #            "interval": "100"}

        qb_dict = eval(msg.payload.decode("utf-8"))
        print('qb_dict:')
        print(qb_dict)
        print(type(qb_dict))
        form = BdnkDataForm(qb_dict)
        # for key,value in qb_dict.items():
        #     print(key + ':' + value)
        if form.is_valid():
            print('saving BdnkData')
            form.save()


def bdnk_device_set(request):
    request.encoding = 'utf-8'
    if 'bdnk_internal_time_s' in request.GET:
        message = '北斗纽扣的消息间隔: ' + request.GET['bdnk_internal_time_s']
    else:
        message = '你提交了空表单！'
    print(message)
    return HttpResponse(message)

if __name__ == '__main__':
    client_loop()


# qb_dict = {"sn": "1234",
#            "imei": "5678",
#            "interval": "178",
#            "led": "1",
#            "enable_shut_off_by_pwrkey": "0",
#            "run_status": "1234",
#            "phone_number": "13677"}
# print(qb_dict)
# print(type(qb_dict))
# BdnkDeviceStatus.objects.create(sn = "1234",
#            imei = "5678",
#            interval= "178",
#            led= "1",
#            enable_shut_off_by_pwrkey="0",
#            run_status="1234",
#            phone_number="13677")
# BdnkDeviceStatus.objects.create(sn = "1234")
# print('create BdnkDeviceStatus')
# # while(1):
# #     pass
# # BdnkDeviceStatus.objects.create(qb_dict)# qb_dict = {"sn": "1234",
# #            "imei": "5678",
# #            "interval": "178",
# #            "led": "1",
# #            "enable_shut_off_by_pwrkey": "0",
# #            "run_status": "1234",
# #            "phone_number": "13677"}
# # print(qb_dict)
# # print(type(qb_dict))
# # BdnkDeviceStatus.objects.create(sn = "1234",
# #            imei = "5678",
# #            interval= "178",
# #            led= "1",
# #            enable_shut_off_by_pwrkey="0",
# #            run_status="1234",
# #            phone_number="13677")
# # BdnkDeviceStatus.objects.create(sn = "1234")
# # print('create BdnkDeviceStatus')
# # # while(1):
# # #     pass
# # # BdnkDeviceStatus.objects.create(qb_dict)