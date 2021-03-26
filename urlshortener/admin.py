from django.contrib import admin
from urlshortener.models import ShortUrl

# Register your models here.
class ShortUrlAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortUrl, ShortUrlAdmin)