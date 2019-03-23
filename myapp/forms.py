from django import forms
from .models import Topic,Entry,BdnkData

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class BdnkDataForm(forms.ModelForm):
    class Meta:
        model = BdnkData
        fields = ['lat', 'long', 'locate_mode', 'bat', 'si', 'elapse']
        # 以下这句把标签给清空了
        # labels = {'lat':'', 'long':'', 'locate_mode':'', 'bat':'', 'si':'', 'elapse':''}
