# Create a class Movie.

# Attributes:
# - title
# - genre
# - rating

# Methods:
# - is_recommended() → returns True if rating is at least 8.

# Tasks:

# - Create 7 movies.
# - Store them in a list.
# - Create a new list containing only recommended movie titles.
# - Print the list.

class Movie():
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def is_recommended(self):
        if self.rating > 8:
            return True
        else:
            return False

movie1 = Movie("Title action", "action", 10)
movie2 = Movie("Title comedy", "Sci-fi", 9)
movie3 = Movie("Title action", "action", 5)
movie4 = Movie("Title romance", "romance", 8)
movie5 = Movie("Title horrer", "horrer", 4)

movies = [movie1, movie2, movie3, movie4, movie5]

recommendec_movies = []

for movie in movies:
    if movie.is_recommended():
        recommendec_movies.append(movie.title)

print(recommendec_movies)