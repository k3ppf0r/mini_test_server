# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
 
# csrf
def post_csrf(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    resp=  render(request, "post.html", ctx)
    resp.set_cookie('lax_cookie','lax_cookie_value',samesite='Lax', httponly=True)
    # 只有这个能带上
    resp.set_cookie('none_cookie','none_cookie_value',samesite='None', httponly=False,secure=True)
    return resp