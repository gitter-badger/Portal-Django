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
    if email:
        user = User(email=email)
        context['headimg'] = user.getGravatar()
    else:
        return infoMsg("请输入email")
    return render_to_response('user/avatar.html', context)

def userUser(request):
    context = {}
    searchable_cols = ('username','id','email');
    colname = "";
    try:
        for sc in searchable_cols:
            if request.GET.get(sc):
                colname = sc;
        if colname != "":
            kwargs = {colname : request.GET.get(colname)}
            user = User.objects.get(**kwargs);
        else:
            return infoMsg("请输入 {0}中的一种".format((sc+" ") for sc in searchable_cols));
    except:
        return infoMsg("用户 {0} 不存在！".format(colname))
    context['headimg'] = user.getGravatar();
    context['user'] = user
    return render_to_response('user/index.html', context);
