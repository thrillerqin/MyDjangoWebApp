'''定义myapp的URL模式'''

# 解决新django中的path不能使用正则表达式
# 新版的path 虽然 取代了 之前的url，但是在写路由的时候不能在路由中直接写正则表达式，不然会找不到页面。
#
# 解决方法
# 使用re_path

# from django.conf.urls import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    # 主页
    # re_path('^$', views.index, name='index'),
    path('', views.index, name='index'),
    # 显示所有主题
    re_path('^topics/$', views.topics, name='topics'),
    # 显示特定主体的文章的页面
    re_path('^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
    # 用于添加新主题的网页
    re_path('^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新文章的页面
    re_path('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name = 'new_entry'),
]

# from django.conf.urls import url
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     # 主页
#     url('^$', views.index, name='index'),
#     # 显示所有主题
#     url('^topics/$', views.topics, name='topics'),
#     # path('^topics/$', views.topics, name = 'topics'),
#     # 显示特定主体的文章的页面
#     url('^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),
#     # 用于添加新主题的网页
#     url('^new_topic/$', views.new_topic, name='new_topic')
# ]