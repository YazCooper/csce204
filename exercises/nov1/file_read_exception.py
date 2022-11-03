#author yaz c




def get_movies():
    movies=[]

    #read the movie file and add each movie to the list
    
    try:
        with open("exercises/nov1/movie.txt") as file:
            for line in file:
                if line.strip() != "":
                #watch = line.strip()
                    movies.append(line.strip())
    except FileNotFoundError:
        print("Sorry, Invalid File Name.")



    return movies


movies = get_movies()


for movie in movies:
    print(movie)