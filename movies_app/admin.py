from django.contrib import admin
from .models import *
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('Series_Title', 'Genre')


class My_Watch_ListsAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie_id')


class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('recommender', 'recommend_to', 'movie')


admin.site.register(Movie, MovieAdmin)
admin.site.register(My_Watch_List, My_Watch_ListsAdmin)
admin.site.register(Recommendations, RecommendationsAdmin)

