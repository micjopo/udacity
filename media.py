import webbrowser # Imports the standard Python class module for launching a new web page.

class Video():
    """ This class provides general information about the video clips. """

    def __init__(self, video_title, poster_image):
        self.title = video_title
        self.poster_image_url = poster_image

class Movie(Video):
    """This class provides a way to store movie-related information."""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] 
    
    def __init__(self, video_title, poster_image, movie_storyline, trailer_youtube):
        Video.__init__(self, video_title, poster_image)
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    """This class provides a way to store tv show-related information."""

    def __init__(self, video_title, poster_image, tvshow_season_episode, trailer_youtube):
        Video.__init__(self, video_title, poster_image)
        self.season_episode = tvshow_season_episode
        self.trailer_youtube_url = trailer_youtube
            
    def get_local_listing(self, listing_website):
        webbrowser.open(self.listing_url)
        
    
