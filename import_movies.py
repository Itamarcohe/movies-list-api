import csv
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
import django
django.setup()
from movies_app.models import Movie

with open('../movies_project/imdb_top_1000.csv', 'rt', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    for row in reader:
        movie = Movie(
            Poster_link=row[0],
            Series_Title=row[1],
            Released_Year=row[2],
            Certificate=row[3],
            Runtime=row[4],
            Genre=row[5],
            IMDB_Rating=row[6],
            Overview=row[7],
            Meta_score=row[8],
            Director=row[9],
            star1=row[10],
            star2=row[11],
            star3=row[12],
            star4=row[13],
            No_of_Votes=row[14],
            Gross=row[15]
        )
        movie.save()

# with open('../../../movies_project/imdb_top_1000.csv', 'rt', encoding='utf-8-sig') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         movie = Movie(
#             Poster_link=row[0],
#             Series_Title=row[1],
#             Released_Year=row[2],
#             Certificate=row[3],
#             Runtime=row[4],
#             Genre=row[5],
#             IMDB_Rating=row[6],
#             Overview=row[7],
#             Meta_score=row[8],
#             Director=row[9],
#             star1=row[10],
#             star2=row[11],
#             star3=row[12],
#             star4=row[13],
#             No_of_Votes=row[14],
#             Gross=row[15]
#         )
#         movie.save()


