from sorting_comparisons import sortByTitle, sortByYear

def test_sortByTitle():
    movies = [
        {"title": "An Inception", "year": 2010, "genres": ["Action", "Adventure", "Sci-Fi"]},
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "A Titanic", "year": 1997, "genres": ["Drama", "Romance"]},
        {"title": "Avengers: Endgame", "year": 2019, "genres": ["Action", "Adventure", "Fantasy"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]}
    ]

    sorted_movies = sortByTitle(movies)
    titles = [movie["title"] for movie in sorted_movies]
    expected_titles = ["Avengers: Endgame", "The Dark Knight", "An Inception", "The Shawshank Redemption", "A Titanic"]
    assert titles == expected_titles



def test_sortByYear():
    movies = [
        {"title": "An Inception", "year": 2010, "genres": ["Action", "Adventure", "Sci-Fi"]},
        {"title": "The Dark Knight", "year": 2008, "genres": ["Action", "Crime", "Drama"]},
        {"title": "A Titanic", "year": 1997, "genres": ["Drama", "Romance"]},
        {"title": "Avengers: Endgame", "year": 2019, "genres": ["Action", "Adventure", "Fantasy"]},
        {"title": "The Shawshank Redemption", "year": 1994, "genres": ["Drama"]}
    ]

    sorted_movies = sortByYear(movies)
    years = [movie["year"] for movie in sorted_movies]
    expected_years = [1994, 1997, 2008, 2010, 2019]
    assert years == expected_years
