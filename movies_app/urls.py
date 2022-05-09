from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('movie_details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('search/', views.search, name='search'),
    path('watch_list', views.my_watch_list_view, name='watch_list'),

    path('my_watch_list/<int:movie_id>', views.watch_list_view, name='my_watch_list'),

    path('recommend_to/<int:movie_id>', views.recommend_a_movie, name='recommend_to'),


    path('recommend_list', views.recommend_list, name='recommend_list'),

    path('respond_to/<int:recommend_id>', views.respond_recommend, name='respond_to'),

]
