"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from community.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^write/', write, name = 'write'),
    #유알엘을 롸이트함수로 보낸 - 그리고 역으로 뷰파일 안에 롸이트 함수를 빌딩한다
    #여기서 네임은 내부적으로만 사용할 이름을 말한다
    #정규표현식 롸이트
    url(r'^list/', list, name='list'),
    #리스트 주소로 접근하면 리스트라는 함수로 가게끔 - 그럼 뷰에 있는 리스트 함수로
    url(r'^view/(?P<num>[0-9]+)/$', view),
    #정규표현식 숫자가 몇번 반복될 수 있다는 뜻, 뷰쓰안에 뷰를 만들고 얘를 처리하도록
]




#저장한것을 보는 리스트를 만들어보





#외부유저들이 접근 가능한 유알엘들이 들어있다