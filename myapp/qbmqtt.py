import paho.mqtt.client as mqtt
import time

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic,BdnkData
from .forms import TopicForm,EntryForm,BdnkDataForm

HOST = "www.ry9r4e4.mqtt.iot.bj.baidubce.com"
PORT = 1883

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
    print("Connected with result code "+str(rc))
    client.subscribe("/Z001/867186030831084/123456789/data")

def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode("utf-8"))
    qb_dict = {	"lat":	"40.823532",
                "long":	"116.284368",
                "locate_mode":	"LBS",
                "bat":	"84",
                "si":	"24",
                "elapse":	"71493",
                "time":	"2019-03-21 13:50:41",
                "interval":	"100"}
    # qb_dict = msg.payload.decode("utf-8")
    print('qb_dict:')
    print(qb_dict)
    print(type(qb_dict))

    qb_dict1111 = eval(msg.payload.decode("utf-8"))
    print('qb_dict1111:')
    print(qb_dict1111)
    print(type(qb_dict1111))
    form = BdnkDataForm(qb_dict1111)
    # for key,value in qb_dict.items():
    #     print(key + ':' + value)
    if form.is_valid():
        print('saving')
        form.save()

if __name__ == '__main__':
    client_loop()