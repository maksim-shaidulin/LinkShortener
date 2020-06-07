from django.http import HttpResponse, Http404
from django.shortcuts import render
# from django.urls import reverse
from .models import Link
import random
import string


def index(request):
    return render(request, 'index.html')


def create(request):
    if 'full_link' not in request.POST:
        return HttpResponse("ERROR: full_link is missing!")

    qs = Link.objects.filter(full_link=request.POST['full_link'])
    if len(qs) != 0:
        # full_link already exists, return already existing link
        # FIXME what if someone want to set own short link name?
        return HttpResponse(qs[0])

    link = Link()
    link.full_link = request.POST['full_link']
    if 'short_link' in request.POST:
        link.short_link = request.POST['short_link']
        if len(link.short_link) != 7:
            return HttpResponse(f"ERROR: Short link must be 7 chars length, but your short link {link.short_link} has length {len(link.short_link)}")
    else:
        link.short_link = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
    link.save()
    return HttpResponse(link)
    # return HttpResponse(f"Short link: {link.short_link}")


def list(request):
    links = Link.objects.order_by('-created_at')[:10]
    return render(request, 'list.html', {'links': links})


def detail(request, link_id):
    try:
        link = Link.objects.get(id=link_id)
    except Http404:
        raise Http404(f"Link with id {link_id} does not exists!")
    return render(request, "detail.html", {"link": link})

def delete(request, link_id):
    pass