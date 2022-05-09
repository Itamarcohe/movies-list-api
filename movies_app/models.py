from django.db import models
from django.contrib.auth.models import User

# Create your models here.
RATING_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class Movie(models.Model):
    Poster_link = models.CharField(max_length=512)
    Series_Title = models.CharField(max_length=512)
    Released_Year = models.CharField(max_length=128)
    Certificate = models.CharField(max_length=100)
    Runtime = models.CharField(max_length=128)
    Genre = models.CharField(max_length=128)
    IMDB_Rating = models.CharField(max_length=128)
    Overview = models.CharField(max_length=2000)
    Meta_score = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    star1 = models.CharField(max_length=100, null=True, blank=True)
    star2 = models.CharField(max_length=100, null=True, blank=True)
    star3 = models.CharField(max_length=100, null=True, blank=True)
    star4 = models.CharField(max_length=100, null=True, blank=True)
    No_of_Votes = models.CharField(max_length=100)
    Gross = models.CharField(max_length=110)

    def __str__(self):
        return self.Series_Title

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'movies'


class My_Watch_List(models.Model):
    movie_id = models.ForeignKey(Movie, models.RESTRICT, null=False, blank=False)
    rate = models.CharField(choices=RATING_CHOICES, max_length=1, null=False, blank=False)
    review_msg = models.CharField(max_length=1024, null=False, blank=False, default='Liked')
    watched_date = models.DateTimeField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='user')

    def __str__(self):
        return f"Review by: {self.user} for: {self.movie_id}"

    class Meta:
        verbose_name_plural = 'watch_list'


class Recommendations(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.RESTRICT)
    recommender = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='recommender')
    recommend_to = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='recommend_to')
    message = models.TextField(max_length=526, blank=True, null=True)
    date_recommended = models.DateField(auto_now_add=True)
    is_watched_by_receiver = models.BooleanField(null=True, blank=True)
    date_watched_by_receiver = models.DateField(null=True, blank=True)
    receiver_rating = models.CharField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.movie} recommended by {self.recommender} to {self.recommend_to}"


    class Meta:
        verbose_name_plural = 'recommendations'

# USER_CHOICES = [user for user in range(User.objects.all())]

# print(len(User.objects.all()))
