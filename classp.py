class Movie:
    '''this code is property of siddharth dixit'''
    def __init__(self,movie, actor, femaleactor, ratings):
        self.movie=movie
        self.actor=actor
        self.femaleactor=femaleactor
        self.ratings=ratings
    def info(self):
        print("Move name  {}".format(self.movie))
        print("Male lead actor is {}".format(self.actor))
        print("Female lead actor is {}".format(self.femaleactor))
        print("Ratings of the movie is {}".format(self.ratings))

movies=[Movie("Raees", "Shahrukh khan", "Mahira khan", "7"),
        Movie("Bajrangi Bhaijaan", "Salman khan", "Kareena Kapoor", "8"),
        Movie("Airlift", "Akshay Kumar", "Nimrat Kaur", "7.5")]

for movie in movies:
    movie.info()
    print()

