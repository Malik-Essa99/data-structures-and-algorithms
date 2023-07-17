data = [
    {"title": "An Inception",
     "year": 2010,
     "genres": ["Action", "Adventure", "Sci-Fi"]},
    
    {"title": "The Dark Knight",
     "year": 2008,
     "genres": ["Action", "Crime", "Drama"]},
    
    {"title": "A Titanic",
     "year": 1997,
     "genres": ["Drama", "Romance"]},
    
    {"title": "Avengers: Endgame",
     "year": 2019,
     "genres": ["Action", "Adventure", "Fantasy"]},
    
    {"title": "The Shawshank Redemption",
     "year": 1994,
     "genres": ["Drama"]}
]

def sortByYear(movies):
    if not movies:
        return[]
    
    result = [movies[0]]

    for movie in movies[1:]: 
        inserted = False 

        for index, sorted_movie in enumerate(result):
            if movie["year"] < sorted_movie["year"]:
                result.insert(index, movie)  
                inserted = True
                break

        if not inserted:
            result.append(movie) 

    return result

def sortByTitle(movies):
    prefixes = ["A ", "An ", "The "]

    def removePrefixes(title):
        for prefix in prefixes:
            if title.startswith(prefix):
                title = title[len(prefix):].strip()
                break
        return title

    sorted_movies = sorted(movies, key=lambda movie: removePrefixes(movie["title"]).lower())
    return sorted_movies


        
sorted_movies = sortByYear(data)

for movie in sorted_movies:
    print(movie)
    
print("*******************************************")
sorted_movies = sortByTitle(data)

for movie in sorted_movies:
    print(movie)