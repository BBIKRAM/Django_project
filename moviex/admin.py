from django.contrib import admin
from .models import gener,movies
# Register your models here.
class generAdmin(admin.ModelAdmin):
    list_display=('id','name')
class moviesAdmin(admin.ModelAdmin):
    list_display=('id','title','cost')



admin.site.register(gener,generAdmin)
admin.site.register(movies,moviesAdmin)
