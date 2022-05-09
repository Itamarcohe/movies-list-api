from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'That User does not exist')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username/Password does not exist')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def logoutUser(reuqest):
    logout(reuqest)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Sorry something went wrong try again')

    return render(request, 'login_register.html', {'form': form})


def home(request):

    movies = Movie.objects.all()
    if 'sort_by_year' in request.GET:
        if request.GET['sort_by_year'] == "desc":
            movies = movies.order_by('Released_Year')
        else:
            movies = movies.order_by('-Released_Year')
    if 'sort_by_rating' in request.GET:
        if request.GET['sort_by_rating'] == "desc":
            movies = movies.order_by('IMDB_Rating')
        else:
            movies = movies.order_by('-IMDB_Rating')
    paginator = Paginator(movies, 32)
    page = request.GET.get('page')
    paged_movies = paginator.get_page(page)
    context = {
        'movies': paged_movies,
    }
    return render(request, 'home.html', context)


def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {'movie': movie}
    return render(request, 'movie_details.html', context)


def search(request):
    query = None
    results = []
    if request.method == "GET":
        query = request.GET.get('search')
        results = Movie.objects.filter(Q(Series_Title__icontains=query) |
                                    Q(Director__icontains=query) |
                                    Q(Genre__icontains=query))
    return render(request, 'search.html', {'query': query, 'results': results})


@login_required(login_url='login')
def my_watch_list_view(request):
    try:
        my_list = [review for review in My_Watch_List.objects.filter(user=request.user)]
        print(my_list)
        context = {'my_list': my_list}
    except:
        return HttpResponse('You must be logged in')

    return render(request, 'watch_list.html', context)


@login_required(login_url='login')
def watch_list_view(request, movie_id):
    if request.method == 'GET':
        form = My_Watch_ListForm(initial={'user': request.user,
                                   'movie_id': movie_id})

        return render(request, 'watch_list_form.html', {'form': form})
    elif request.method == 'POST':
        form = My_Watch_ListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'watch_list_form.html', context)


@login_required(login_url='login')
def recommend_a_movie(request, movie_id):
    if request.method == 'GET':
        form = Recommend_a_movieForm(initial={'recommender': request.user,
                                              'movie': movie_id})
        context = {'form': form}
        return render(request, 'recommend_to_form.html', context)
    elif request.method == 'POST':
        form = Recommend_a_movieForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {'form': form}
            return render(request, 'recommend_to_form.html', context)


@login_required(login_url='login')
def recommend_list(request):
    recommneds = Recommendations.objects.filter(recommend_to=request.user)
    context = {'recommneds': recommneds}
    return render(request, 'respond_recommend_list.html', context)


@login_required(login_url='login')
def respond_recommend(request, recommend_id):
    recommend = Recommendations.objects.get(id=recommend_id)
    if request.method == 'GET':
        form = Respond_Recommend(instance=recommend)
        context = {'form': form}
        return render(request, 'respond_to_form.html', context)
    elif request.method == 'POST':
        form = Respond_Recommend(data=request.POST, instance=recommend)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'respond_to_form.html', {'form': form})

