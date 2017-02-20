import webbrowser

class Video() :
    """This class provides a way to initialize video related information"""
    #Initialize of instance attributes
    def __init__(self, title, duration) :
        self.title = title
        self.duration = duration

#Inherite from Video class
class Movie(Video) :
    """ This class provides a way to store movie related information"""
    #class variables
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    #Initialize of instance attributes
    def __init__(self, movieTitle, movieStoryLine, posterImage, youtubeTrailer, duration) :
        #Calling parent constructor to construct the common attributes
        Video.__init__(self, movieTitle, duration)

        #instance variables
        self.storyline           = movieStoryLine
        self.poster_image_url    = posterImage
        self.trailer_youtube_url = youtubeTrailer

    #function to show trailer
    def showTrailer(self) :
        webbrowser.open(self.trailer_youtube_url)        
