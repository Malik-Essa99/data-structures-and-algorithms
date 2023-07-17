# Sorting Comparisons
### Author: Malik Al Hudrub
### How to initialize/run your application:
python data-structures-and-algorithms/Sorting-Comparisons/sorting_comparisons.py

### Testing 
### How do you run tests?
+ cd data-structures-and-algorithms/Sorting-Comparisons/tests 
+ pytest tests.py

### Algorithm:

``` 

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

```

### Efficency:

#### sortByYear:

Time: O(n^2) 

Space: O(n)

#### sortByTitle:

Time: O(n log (n)) 

Space: O(n)
