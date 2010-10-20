from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from shitcal.models import Shit
from auth.models import User

def stats(request):
    all_users = User.objects.filter(active=True)
    all_shits = Shit.objects.all()
    num_users = all_users.count()
    num_shits = all_shits.count()

    context = {
        'num_users': num_users,
        'num_shits': num_shits,
    }
    template_name = 'shitcal/stats.html'
    return render_to_response(template_name, context,
        context_instance = RequestContext(request))

def profile(request, user):
    user = get_object_or_404(User, username=username)
    shits = Shit.objects.filter(user=user)
    context = {
        'user': user,
        'shits': shits,
    }
    template_name = 'shitcal/profile.html'
    return render_to_response(template_name, context,
        context_instance = RequestContext(request))
