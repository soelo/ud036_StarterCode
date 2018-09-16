import webbrowser

class Movie():
    ##list of instance variables for movie Class:
    def __init__(self,movie_title, release_date, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.date = release_date
    ## function to display trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
