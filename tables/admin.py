from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MovieGenres)
admin.site.register(MovieFormat)
admin.site.register(MovieCategory)
admin.site.register(MovieLanguage)
admin.site.register(MovieTime)
admin.site.register(MovieRating)
admin.site.register(MovieCast)
admin.site.register(Movie)
admin.site.register(MovieSeats)
admin.site.register(MovieTicket)