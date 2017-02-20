import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio", 130)
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY", 180)
#print(avatar.storyline)
#avatar.showTrailer()

minions = media.Movie("Minions",
                      "Signature characters of the Despicable Me series",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "https://www.youtube.com/watch?v=P9-FCC6I7u0", 120)
#minions.showTrailer()

school_of_rock = media.Movie("School of Rock",
                      "Use rock music to learn",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                      "https://www.youtube.com/watch?v=XCwy6lW5Ixc", 110)

kungfu_yoga = media.Movie("Kungfu Yoga",
                      "A treasure seeking with kungfu and yoga",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Kung_Fu_Yoga_poster.jpeg/220px-Kung_Fu_Yoga_poster.jpeg",
                      "https://www.youtube.com/watch?v=2UTnMVS6G5Y", 115)

xander_cage = media.Movie("xXx Xander Cage",
                      "Secret agent",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/9/9c/Xxx_return_of_xander_cage_film_poster.jpeg/220px-Xxx_return_of_xander_cage_film_poster.jpeg",
                      "https://www.youtube.com/watch?v=MQEFmHsseaU", 130)

#define a array list
movies = [toy_story, avatar, minions, school_of_rock, kungfu_yoga, xander_cage]
fresh_tomatoes.open_movies_page(movies)

