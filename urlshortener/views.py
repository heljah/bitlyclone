from django.shortcuts import render
from django.http import HttpResponseNotFound
from urlshortener.models import ShortUrl
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
@never_cache
def short_url(request, slug):
    if not slug:
        return HttpResponseNotFound("Page not found")
    else:
        url = get_object_or_404(ShortUrl, slug=slug)
        return redirect(url.url)