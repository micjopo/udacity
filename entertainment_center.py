# Importing the fresh_tomatoes Python class module to launch the webpage.
import fresh_tomatoes

# Importing the media Python module to use the Movie() class.
import media

""" The following class instances contain information about each movie and its trailer. Each instance
 inherits functions from class Movie(). Each instance contains a title, a short storyline blurb,
 and links to the poster image and trailer clip."""

toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "A story of a boy and his toys that come to life.",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline) <- used to test print output of the Toy Story storyline string.

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "A marine on an alien planet.",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
# print(avatar.storyline) <- used to test print output of the Avatar storyline string.
# avatar.show_trailer() <- used to test launching the YouTube movie trailer on a new web page.

the_goonies = media.Movie("The Goonies",
                          "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Goonies.jpg",
                          "A bunch of kids go treasure-hunting and hijinks ensue.",
                          "https://www.youtube.com/watch?v=hJ2j4oWdQtU")
# the_goonies.show_trailer() <- used to test launching the YouTube movie trailer on a new web page.

school_of_rock = media.Movie("School of Rock",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "Using rock music to learn.",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "A rat is a chef in Paris.",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "Going back in time to meet authors.",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("The Hunger Games",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "A really real reality show.",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

breaking_bad = media.TvShow("Breaking Bad",
                            "https://upload.wikimedia.org/wikipedia/en/6/61/Breaking_Bad_title_card.png",
                            "Season 5",
                            "https://www.youtube.com/watch?v=XZ8daibM3AE")                           

# the "movies" variable contains the class instances in an array to be used in generating the info on the web page.
trailers = [toy_story, avatar, the_goonies, school_of_rock, ratatouille,
          midnight_in_paris, hunger_games, breaking_bad]

fresh_tomatoes.open_movies_page(trailers)# opens the movie trailer web page in the web browser.

# print(media.Movie.VALID_RATINGS) <- test for printing array output of VALID RATINGS class variable

print(media.Movie.__doc__) # prints doc output string explaining the purpose of the Movie() class.
