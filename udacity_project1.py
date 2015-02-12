# Udacity Full-Stack Web Developer Microdegree Project 1 Submission
# Create a list of Movies and submit it to open_movies_page() in 
# fresh_tomatoes.py so that it is displayed properly.

# open_movies_page() expects the following properties on each movie:
#   trailer_youtube_url
#   title
#	poster_image_url

import fresh_tomatoes

class movie:
	title = ""
	poster_image_url = ""
	trailer_youtube_url = ""
	
	def __init__ (self, Title, PosterUrl, YoutubeTrailerUrl):
		self.title = Title
		self.poster_image_url = PosterUrl
		self.trailer_youtube_url = YoutubeTrailerUrl

Yojimbo = movie("Yojimbo", \
				"http://ia.media-imdb.com/images/M/MV5BMTIwMzExNjEzM15BMl5BanBnXkFtZTcwODk2NDE0MQ@@._V1_SY317_CR5,0,214,317_AL_.jpg", \
				"https://www.youtube.com/watch?v=y_1iT_GmHTE")
movies = [Yojimbo]

fresh_tomatoes.open_movies_page(movies)