import requests

api_key = "adb8637aa3e6e08b7210619c9fb9cae8"

endpoint = "https://api.themoviedb.org/3/discover/movie"

params = f"?include_adult=false&include_video=false&language=en-US&page=1&sort_by=vote_count.desc&year=2023"

url = f"{endpoint}{params}&api_key={api_key}"

headers = {"accept": "application/json"} 

#Faz a requisição GET para a url
# salva na variável response o resultado na busca do TMDB

response = requests.get(url, headers=headers)

#print(response.txt)

data = response.json()

page = data['page']

print(f"page: {page}")

filme1 = data['results'][0]

#Obtem apenas o titulo do primeiro filme
print(filme1['original_title'])

#IMPRIMIR o título de todos os filmes em "data"

results = data['results']
print("="*20)
for movie in results:
    print(movie['original_title'])
    print(movie['id'])
    print(movie['vote_count'])
    print("------------")
print(f"Total:{len(results)}")

# Obter os gêneros

end = "https://api.themoviedb.org/3/genre/movie/list"
params = "?language=en&api_key=" + api_key
url = f"{end}{params}"

response = requests.get(url)
data = response.json()

if 'genres' in data:
    genres = data['genres']
    print("="*20)
    for genre in genres:
        print(genre['name'])
        print("-------")
else:
    print("Não foi possível obter os gêneros da API.")
    
