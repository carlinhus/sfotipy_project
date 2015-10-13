# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import TemplateView
from sfotipy.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.template import RequestContext
from django.http import Http404



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'user': self.get_user()})

        return context

    def get_user(self):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect("landing")

def landing_view(request):
    return render_to_response("landing.html", {}, context_instance=RequestContext(request))


def login_view(request):
    if(request.method != "POST"):
        raise Http404("Invalid request method.")

    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect("landing")
        else:
            return render_to_response("landing.html", {"loginError" : "Your account has benn disabled."}, context_instance=RequestContext(request))
    else:
        # the authentication system was unable to verify the username and password
        return render_to_response("landing.html", {"loginError" : "Wrong username and/or password"}, context_instance=RequestContext(request))
