from django.shortcuts import render
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect


def render_tamplate(tpl, dt, request):
    """
    :param tpl: html template
    :param dt: dictionary to send
    :param request: HTTP request
    :return: HTML with base
    """
    dct = {}
    dct.update(dt)
    return render(request, tpl, dct)


def render_login(tpl, request):
    """
    :param tpl: html template
    :param request: HTTP request
    :return: HTML with base
    """
    return login(request, tpl)


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/admin-panel')
    else:
        return render_login('login.html', request)


def admin_panel(request):
    if request.user.is_authenticated:
        return render_tamplate('index.html', {}, request)
    else:
        return render_login('login.html', request)