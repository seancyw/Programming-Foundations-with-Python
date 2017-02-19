import webbrowser

class Movie() :
    def __init__(self, movieTitle, movieStoryLine, posterImage, youtubeTrailer) :
        self.title               = movieTitle
        self.storyline           = movieStoryLine
        self.poster_image_url    = posterImage
        self.trailer_youtube_url = youtubeTrailer

    def showTrailer(self) :
        webbrowser.open(self.trailer_youtube_url)        
