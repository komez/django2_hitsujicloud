from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import user_logged_out
# Create your views here.
@login_required(login_url = '/accounts/login/')
def index(request):

    #とりあえず
    messages = 'messages'
    checkform = 'check_form'
    searchform = 'search_form'
    #共通のparam
    params = {
        'login_user' : request.user,
        'contents' : messages,
        'check_form' : checkform,
        'search_form' : searchform,
    }

    return render(request, 'games/index.html', params)

def logout_view(request):
    user_logged_out(request)