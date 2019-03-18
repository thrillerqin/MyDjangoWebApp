from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    '''网站的主页'''
    return render(request, 'myapp/index.html')

@login_required
def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'myapp/topics.html', context)

@login_required
def topic(request, topic_id):
    '''显示单个主题及其所有的条目'''
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'myapp/topic.html', context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据,对数据进行处理
        form = TopicForm(request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        # form.save()
        return HttpResponseRedirect(reverse('myapp:topics'))

    context = {'form': form}

    return render(request, 'myapp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    '''在特定主题下添加新文章'''
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
    if form.is_valid():
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        return HttpResponseRedirect(reverse('myapp:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'myapp/new_entry.html', context)