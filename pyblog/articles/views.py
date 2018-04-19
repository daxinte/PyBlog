from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone


from .models import Comment

def detail(request, comment_id):
    return HttpResponse("You're looking at comment %s." % comment_id)

def index(request):
    latest_comment_list = Comment.objects.order_by('-pub_date')[:5]
    output = ', '.join([c.comment_text for c in latest_comment_list])
    return HttpResponse(output)