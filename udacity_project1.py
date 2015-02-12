# Udacity Full-Stack Web Developer Microdegree Project 1 Submission
# Create a list of Movies and submit it to open_movies_page() in 
# fresh_tomatoes.py so that it is displayed properly.

import fresh_tomatoes

# open_movies_page() expects the following properties on each movie:
#   trailer_youtube_url
#   title
#   poster_image_url

class movie:
	title = ""
	poster_image_url = ""
	trailer_youtube_url = ""
	released_in = ""
	rated = ""
	
	# We're using the __init__ function as a constructor here to make
	# instantiating new movie objects a little easier.
	
	def __init__ (self, Title, PosterUrl, YoutubeTrailerUrl, ReleasedIn, Rating):
		self.title = Title
		self.poster_image_url = PosterUrl
		self.trailer_youtube_url = YoutubeTrailerUrl
		self.released_in = ReleasedIn
		self.rated = Rating

Yojimbo = movie("Yojimbo", \
                "http://ia.media-imdb.com/images/M/MV5BMTIwMzExNjEzM15BMl5BanBnXkFtZTcwODk2NDE0MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg", \
                "https://www.youtube.com/watch?v=y_1iT_GmHTE", \
                "1961", "Unrated")
Sanjuro = movie("Sanjuro", \
                "http://ia.media-imdb.com/images/M/MV5BMTQ2MzYwNzUzMV5BMl5BanBnXkFtZTgwMDM3NTU3MzE@._V1_SY317_CR0,0,214,317_AL_.jpg", \
                "https://www.youtube.com/watch?v=Uq_rSsbhQnE", \
                "1962", "Unrated")
SevenSamurai = movie("Seven Samurai", \
                     "http://ia.media-imdb.com/images/M/MV5BMTc5MDY1MjU5MF5BMl5BanBnXkFtZTgwNDM2OTE4MzE@._V1_SY317_CR6,0,214,317_AL_.jpg", \
                     "https://www.youtube.com/watch?v=7mw6LyyoeGE", \
                     "1954", "Unrated")

# Now we just add the movies to the Movies list, then give it to 
# open_movies_page() in fresh_tomatoes.py

movies = [Yojimbo, Sanjuro, SevenSamurai]

fresh_tomatoes.open_movies_page(movies)