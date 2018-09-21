import webbrowser
'''creates a class Movie() to display on fresh_tomatoes website'''


class Movie():
    # creating the list of instance variables for movie Class
    # Variables: movie_title is the full name of the movie.
    # movie_storyline is a brief sentence to describe the plot.
    # poster_image is the whole URL for a poster image.
    # trailer_youtube is the trailer video found on youtube.com.
    # release_date is the date the movie was released in the United States.
    def __init__(self, movie_title, release_date, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.date = release_date

    # function to display trailer on mouse click
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
