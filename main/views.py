from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import *
from main.models import *

# Utils
def infoMsg(content="Hi", url=None, title=None):
    context = {
        'title':title,
        'content':content,
        'url':url,
    }
    return render_to_response("msg.html", context);

# Create your views here.
def index(request):
    return render_to_response('index/index.html');

def userAvatar(request, email):
    context = {}
    tmplt = Template('<img src="{{headimg}}">')
    if email:
        user = User(email=email)
        context['headimg'] = user.getGravatar()
    else:
        return infoMsg("请输入email")
    return render_to_response(tmplt, context)

def userUser(request):
    context = {}
    searchable_cols = ('username','id','email');
    try:
        for sc in searchable_cols:
            if request.GET.get(sc):
                kwargs = {sc:keyword}
                user = User.objects.get(**kwargs);
        if not user:
            return infoMsg("请输入 {0}中的一种".format((sc+" ") for sc in searchable_cols));
    except:
        return infoMsg("用户 " + keyword + " 不存在！")
    context['headimg'] = user.getGravatar();
    context['user'] = user
    return render_to_response('user/index.html', context);
