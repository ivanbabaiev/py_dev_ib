from django.shortcuts import render_to_response


from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main:index', args=()))


def custom_404_server_error(request):
    """
    Call 404.html
    """
    response = render_to_response('main/404.html')
    response.status_code = 404
    return response


def custom_500_server_error(request):
    """
    Call 500.html
    """
    response = render_to_response('main/500.html')
    response.status_code = 500
    return response
