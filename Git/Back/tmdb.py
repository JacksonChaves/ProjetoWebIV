from fastapi import FastAPI
import requests
import uvicorn
# pip install fastapi uvicorn requests


api_key = "adb8637aa3e6e08b7210619c9fb9cae8"

genres = [
    {'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

def get_json(endpoint, params=None):
    """fornecido o endpoint faz o request e rerorna
    o resultado en json"""
    url = f"https://api.themoviedb.org/3{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()

# retorna o nome do genero de acordo com o id
def get_genero_id(id):
    for genre in genres:
        if genre['id'] == id:
            #print(id, genre['name'])
            return genre ['name']
    return None

# teste:
#genre_name = get_genero_id(878)  #Action
#print(878, "\n", genre_name)

# busca filme pelo título
def get_movie_by_name(name: str):
    data = get_json(
        "https://api.themoviedb.org/3/search/movie",
        f"?query={name}"
    )
    return data

# busca artisa pelo nome
def get_artist_by_name(name: str):
    data = get_json(
        "https://api.themoviedb.org/3/search/person",
        f"?query={name}"
    )
    return data

# implementar API usando FASTAPI
# endpoint que retorna 5 filmes recomendados da semana 

app = FastAPI()

@app.get('/week')
def get_week_movies():
    data = get_json(
        "https://api.themoviedb.org/3/trending/movie/week?language=en-US",
        ""
    )
    five_movies: [str] = []
    for movie in data['results']:
        five_movies.append(movie)
        if len(five_movies) == 5:
            break
    return five_movies

def filmes_populares():
    """Obtem os filmes mais populares usando endpoint discover"""
    data = get_json(
        "https://api.themoviedb.org/3/discover/movie",
        "?sort_by=vote_count.desc&language=en-US"
    )
    results = data['results']
    print("=" * 20)
    for movie in results:
        print(movie['original_title'])
        print(movie['id'])
        print(movie['genre_ids'])
        print(movie['vote_count'])
        print("----")

    print(f"Total: {len(results)}")
    
if __name__ == "__main__":
    filmes_populares()

    # Obter o nome dos generos
     
    end = f"https://api.themoviedb.org/3/genre/movie/list"
    params = "?language=en"
    url = f"{end}{params}&api_key={api_key}"
    #imprimir os filmes (titulo) e o nome dos generos
    uvicorn.run("tmdb2:app", host="127.0.0.1", port=8000, reload=True)