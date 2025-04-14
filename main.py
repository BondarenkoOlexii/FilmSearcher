import requests



Key_API = "0ed0bb382f81d8c9f11cad42bf2d282b"
link = "https://api.themoviedb.org/3/discover/movie?"
genres_link = f"https://api.themoviedb.org/3/genre/movie/list?api_key={Key_API}&language=uk-UA"

headeres = {
    "accept" : "application/json",
    "Authorization" : "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZWQwYmIzODJmODFkOGM5ZjExY2FkNDJiZjJkMjgyYiIsIm5iZiI6MTc0MzQxNDE1OC43ODEsInN1YiI6IjY3ZWE2MzhlNjFjYWMyYjNhM2Y2ZjdlMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-1w7K5my6GNYPMLObQsHNbIOxdZ32wG2gwyLNCJcqso"
}

def api_request(list_of_genres, number_of_page):
    params = {
        "apikey": Key_API,
        "include_adult": "false",
        "language": "en-US",
        "page": number_of_page,
        "with_genres": list_of_genres
    }

    main_responce = requests.get(link, headers=headeres, params=params)

    if main_responce.status_code == 200:
        data = main_responce.json()
        return data
    else:
        return(f"Error {main_responce.status_code}")

def films_titles(file):
    list_of_titles = []
    for dicts in file["results"]:
        list_of_titles.append(dicts["title"])
    return list_of_titles






