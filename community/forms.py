#이 forms.py는 내가 만들어낸거다 손으로 직접,
#그냥 주어지는 것이 아니


from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        #신기하다 이거 인스턴스만들어내는 작업이 아니다 그저 모델 이꼬르 알티클이다
        fields= ['name', 'title', 'contents', 'url', 'email']
        #표시할 필드명을 나열한다 이것은 모델에 있는 필드명이 되어야한다

        #근데 이 폼을 어떻게 전달할꺼냐? - 뷰에서 생성가능 뷰로 다시 간다


        #데이타를 만들고 폼을만들고 데이타를 데이타베이스에 저장하는것
