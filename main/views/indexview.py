from django.shortcuts import render_to_response, redirect
from main.models import *
import util.ctrl

# Create your views here.
def index(request):
    context = {'request': request}
    if util.ctrl.isMobile(request):
        return render_to_response('index/index-m.html', context);
    return render_to_response('index/index.html', context);

def indexSettheme(request):
    '''保存/清除用户的 theme 到 cookies 里'''
    loginuser = request.session.get('loginuser')
    if loginuser:
        try:
            user = User.objects.get(id=loginuser['id'])
        except User.DoesNotExist:
            return util.ctrl.infoMsg("您查找的用户 id：{id} 并不存在".format(id=str(loginuser['id'])));
    # get history.back
    if 'HTTP_REFERER' in request.META:
        href_back = request.META.get('HTTP_REFERER')
        response = redirect(href_back)
    else:
        response = redirect('/')
    # CONSTANTS
    theme_name_pool = ("cerulean", "cosmo", "cyborg", "darkly", "flatly", "journal", "lumen", "paper", "readable", "sandstone", "simplex", "slate", "spacelab", "superhero", "united", "yeti")
    theme_key = 'theme'
    # get input
    theme_name = request.GET.get('name')
    if not theme_name: # 清除已设置的主题
        response.delete_cookie(theme_key)
    else: # 设置主题
        theme_name = theme_name.lower()
        if theme_name not in theme_name_pool:
            return util.ctrl.infoMsg("您请求的主题：{theme_name} 不存在".format(theme_name=theme_name), title="设置主题失败")
        oneweek = 60*60*24*7
        response.set_cookie(theme_key, theme_name, max_age=oneweek)
    # add exp if logged in.
    if user:
        theme_name_smart = theme_name or '默认主题'
        userexp, created = UserExp.objects.get_or_create(userid=user.id, category='user')
        userexp.addExp(2, '尝试主题：{theme_name}'.format(theme_name=theme_name_smart.title()))
    return response
