from django.db import models

# Create your models here.


#모델은 기본적으로 클래쓰로 생성이 된
#그리고 그 클래쓰는 모델을 상속한다
class Article(models.Model):
    name = models.CharField(max_length=50)
    #캐릭터필드
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

#이 모델로 폼을 어떻게 만들까?
#이 아티클은 데이타베이스다