import media
import fresh_tomatoes


#instance of Movie for "Toy Story" movie
toy_story=media.Movie("Toy Story",
                                    "Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz",
                                    "Toy.jpg",
                                    "https://www.youtube.com/watch?v=KYz2wyBy3kc",)
#instance of Movie for "Avatar" movie
avatar=media.Movie("Avatar",
                               "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.",
                               "avatar.jpg",
                               "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#instance of Movie for "Swadesh" movie
Swadesh=media.Movie("Swadesh",
                                   "Mohan, a project manager who is employed with NASA, travels to India to take his nanny along with him. Little does he know that this journey will change his life forever",
                                   "swadesh.jpg",
                                   "https://www.youtube.com/watch?v=NC7GuohSdWA")
#instance of Movie for "Dangal" movie
Dangal=media.Movie("Dangal",
                               "Former wrestler Mahavir Singh Phogat (Aamir Khan) trains young daughters Geeta (Fatima Sana Shaikh) and Babita (Sanya Malhotra) to follow in his footsteps and become world-class grapplers",
                               "dangal.jpg",
                               "https://www.youtube.com/watch?v=x_7YlGv9u1g")
#instance of Movie for "Jolly LLB 2" movie
Jolly= media.Movie("Jolly LLB 2",
                            "An ambitious lawyer (Akshay Kumar) finds himself in a battle with a ruthless advocate after making an innocent mistake.",
                            "jolly.jpg",
                           "https://www.youtube.com/watch?v=q07SQFmL4rM")
#instance of Movie for "Kaabil" movie
kaabil= media.Movie("Kaabil",
                               "This is the story of a man who lived, laughed and loved just like everyone in this world. Until one day, a terrible tragedy struck. Driven by the fire of vengeance, nothing will stop him. Not even the fact that he has been blind since birth",
                               "kabil.jpg",
                               "https://www.youtube.com/watch?v=q07SQFmL4rM")

movies=[Swadesh,Dangal,Jolly,kaabil,toy_story,avatar,]
fresh_tomatoes.open_movies_page(movies)
