import media
import fresh_tomatoes

movies = []

spiderman = media.Movie(
    "Spider-Man: Homecoming",
    ("Peter Parker, with the help of his mentor Tony Stark, tries to balance "
     "his life as an ordinary high school student in New York City while "
     "fighting crime as his superhero alter ego Spider-Man when a new threat "
     "emerges."),
    ("https://cdn.vox-cdn.com/uploads/chorus_asset/file/"
     "8571017/spider_man_poster.jpg"),
    "https://www.youtube.com/watch?v=rk-dF1lIbIg"
)
movies.append(spiderman)

thor = media.Movie(
    "Thor: Ragnarok",
    ("Imprisoned, the mighty Thor finds himself in a lethal gladiatorial "
     "contest against the Hulk, his former ally. Thor must fight for survival "
     "and race against time to prevent the all-powerful Hela from destroying "
     "his home and the Asgardian civilization."),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/"
     "Thor_Ragnarok_poster.jpg/220px-Thor_Ragnarok_poster.jpg"),
    "https://www.youtube.com/watch?v=ue80QwXMRHg"
)
movies.append(thor)

guardians = media.Movie(
    "Guardians of the Galaxy vol. 2",
    ("The Guardians must fight to keep their newfound family together as they "
     "unravel the mystery of Peter Quill's true parentage."),
    ("https://upload.wikimedia.org/wikipedia/en/thumb/9/95/"
     "GotG_Vol2_poster.jpg/220px-GotG_Vol2_poster.jpg"),
    "https://www.youtube.com/watch?v=4hdv_6gl4gk"
)
movies.append(guardians)

ironman = media.Movie(
    "Iron Man 3",
    ("When Tony Stark's world is torn apart by a formidable terrorist called "
     "the Mandarin, he starts an odyssey of rebuilding and retribution."),
    "http://cdn.movieweb.com/img.teasers.posters/FI9EvebisBUacc_378_a.jpg",
    "https://www.youtube.com/watch?v=aV8H7kszXqo"
)
movies.append(ironman)

captain = media.Movie(
    "Captain America: Civil War",
    ("Political interference in the Avengers' activities causes a rift "
     "between former allies Captain America and Iron Man."),
    "http://i.imgbox.com/PZ6asnjX.jpg",
    "https://www.youtube.com/watch?v=xnv__ogkt0M"
)
movies.append(captain)

strange = media.Movie(
    "Doctor Strange",
    ("While on a journey of physical and spiritual healing, a brilliant "
     "neurosurgeon is drawn into the world of the mystic arts."),
    ("http://vignette2.wikia.nocookie.net/marvelcinematicuniverse/images/a/a4/"
     "DS_Endless_Possibilities_Poster.jpg/revision/latest?cb=20160909202223"),
    "https://www.youtube.com/watch?v=HSzx-zryEgM"
)
movies.append(strange)


fresh_tomatoes.open_movies_page(movies)
