from django.contrib import admin
from .qbmqtt import client_loop

# Register your models here.
from myapp.models import Topic, Entry, BdnkData

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(BdnkData)


# print('qinbao admin,mqtt client start')
# client_loop()