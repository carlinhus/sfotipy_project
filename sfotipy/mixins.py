# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.text import slugify

class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        count = 2

        slug = slug_text
        while(model._default_manager.filter(slug=slug).exists()):
            slug = '{0}-{1}'.format(slug_text, count)

        return slug