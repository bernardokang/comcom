from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        #(method)변수가 포스트일수도 있고 겠일수도 있고 한다 포스트일 경우에,
        form = Form(request.POST)
        #리퀘스트 메쏘드가 포스트일 경우에 포트스를 그대로 폼에 넣는다
        if form.is_valid():
            #폼에 있는 데이터가 유효하다면
            form.save()
            #세이브를 한다(중요!!), 폼에 데이타를 넣고 다시 sql작성하고 쿼리를 날리는 작업이 단순화됨
        articleList = Article.objects.all()
        #아티클 데이타베이스테이블의 모든 컬럼을 가져온다 그것을또 아티클리스트에 저장한다
        return render(request, 'list.html', {'articleList':articleList})

    else:
        form = Form()
    #엘쓰블럭 위치확인

    #인자가 request(요청이 담긴다)
    # form = Form() 에라이 이걸왜 또썻을까 멍청멍청
    #폼을 생성한다
    #그리고 html에 전달한다 어떻게?
    return render(request, 'write.html',{'form':form})
#폼버튼을 누르면 포스트가 생성된다 포스트가 발생한다

#전달하고자 하는 변수명을 쓰고, 변수를 그대로 넣는다 그러면 write.html에 폼이 날아온다
#write.html로 보낸다, 그것을 렌더링한다


def list(request):
    articleList = Article.objects.all()
    #아티클 데이타베이스테이블의 모든 컬럼을 가져온다 그것을또 아티클리스트에 저장한다
    return render(request, 'list.html', {'articleList':articleList})
    #리스트쩜 에치티엠엘에 {}로 된 변수가 전달이 된다


#이제 list.html을 만들어도 됩니다


def view(request, num="1"):
    article = Article.objects.get(id=num)
    #전달된 넘이 겟뒤로 들어간다
    #아티클(모델)에서 가져오겠다
    #아이템 하나를 가져오는데 그 아이디가 넘이다
    return render(request, 'view.html',{'article':article})
#뒷꼬랑지는 변수처리인듯