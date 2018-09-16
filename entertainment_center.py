import fresh_tomatoes
import media

tag = media.Movie("Tag","Friday, June 15",
                  "Friends keep a game of tag going for decades",
                  "https://upload.wikimedia.org/wikipedia/en/6/6f/Tag_%282018_film%29.png",
                  "https://www.youtube.com/watch?v=kjC1zmZo30U")
mm2 = media.Movie("Mamma Mia: Here We Go Again!",
                  "Friday, July 20",
                  "A sequel to the hit musical",
                  "https://upload.wikimedia.org/wikipedia/en/b/be/Mamma_Mia%21_Here_We_Go_Again.png",
                  "https://www.youtube.com/watch?v=XXGKPpK1Nhk&feature=player_embedded_uturn")
spy = media.Movie("The Spy Who Dumped Me","Friday, August 3",
                  "Audrey discovers her ex was a secret agent",
                  "https://upload.wikimedia.org/wikipedia/en/2/25/The_Spy_Who_Dumped_Me.png",
                  "https://www.youtube.com/watch?v=CXkUaaVrB_s")
guernsey = media.Movie("The Guernsey Literary and Potato Peel Pie Society",
                       "Friday, August 10","The story of a book club formed during WW2",
                       "https://upload.wikimedia.org/wikipedia/en/2/28/The_Guernsey_Literary_and_Potato_Peel_Pie_Society.png",
                       "https://www.youtube.com/watch?v=HTDNGv61-Dk")
asians = media.Movie("Crazy Rich Asians",
                     "Wednesday, August 15",
                     "Rachel visits Singapore with her boyfriend who has been hiding something",
                     "https://upload.wikimedia.org/wikipedia/en/b/ba/Crazy_Rich_Asians_poster.png",
                     "https://www.youtube.com/watch?v=ZQ-YX-5bAs0")
favor = media.Movie("A Simple Favor",
                    "Friday, September 14",
                    "Stephanie's best friend disappears",
                    "https://upload.wikimedia.org/wikipedia/en/5/5c/A_Simple_Favor.png",
                    "https://www.youtube.com/watch?v=rAqMlh0b2HU")
movies = [tag,mm2,spy,guernsey,asians,favor]
fresh_tomatoes.open_movies_page(movies)
