from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import FetchedValue
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import uvicorn
from tmdb import get_json
from fastapi.middleware.cors import (CORSMiddleware)

app = FastAPI()

# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1/5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_artista/{name}")
async def get_artista(name: str):
    """
    obtem lista de artista pelo nome e popularidade
    """    
    data = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )
    
    results = data['results']
    filtro = []
    from pprint import pprint
    
    for artist in results:
        data2 = get_json("/person/" f"{artist['id']}?")
        pprint(data2)
        filtro.append({
            'id': artist['id'],
            'name': artist['name'],
            'rank':artist['popularity'],
            'biography': data2['biography'],
            'birthday': data2['birthday'],
            "image":
                f"https://image.tmdb.org/t/p/w185{artist['profile_path']}"
            ''
            
        })
    # ordenar filtro pelo atributo rank
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    return filtro

# users


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3 ENDPOINTS

#Criar novo usuario
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

#Apresentar todos usuários
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

#Apresentar um usuário
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Atualizar usuário
# @app.put("/users/{user_id}", response_model=schemas.User)
# async def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
#     # antes de atualizar verificar se o usuário existe
#     db_user = crud.get_user(db, user_id)
#     #testa se o db_user existe
#     if db_user is None:
#          raise HTTPException(status_code=404, detail="User not found")
    
#     updated_user = crud.update_user(db, user_id, user_update)
#     return updated_user
#Deletar usuário
@app.delete("/users/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = crud.delete_user(db, user_id)
    return deleted_user

# Favoritar filme
@app.post("/favoritos/", response_model=schemas.Favoritos)
async def favoritar_filme(favorito: schemas.Favoritos, db: Session = Depends(get_db)):
    return crud.favoritar(db=db, favorito=favorito)


@app.get("/favoritos/", response_model=list[schemas.Favoritos])
async def favoritar_filme(user_id: str, db: Session = Depends(get_db)):
    return crud.get_favorito_by_tmdb_id(db, user_id)

@app.delete("/favoritos/{tmdb_id}", response_model=schemas.Favoritos)
async def delete_favorito(tmdb_id: str, db: Session = Depends(get_db)):
    db_favoritos = crud.get_favorito_by_tmdb_id (db, tmdb_id)
    if db_favoritos is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_favorito=crud.delete_favorito(db, tmdb_id)
    return deleted_favorito

# =========================================================================
# Atividade 1

@app.get("/filmes/{title}")
async def find_movie(title: str):

    #procura filme pelo titulo e ordena pelos mais populares
    
    data = get_json("/search/movie", f"?query={title}&language=en-US")

    filtro=[]
    results = data['results']
    

    for title in results:
        
        filtro.append({
            'title': title['title'],
            'rank':title['popularity'],
            'id': title['id'],
            "image":
                f"https://image.tmdb.org/t/p/w185{title['poster_path']}",
            }
            
    
        )

    filtro.sort(reverse = True, key=lambda title:title['rank'])

    return filtro

# =========================================================================
# Atividade 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """
    busca os filmes mais populares de um artista
    Exemplo: /artista/filmes?personId=1100
    """
    
    person_data = get_json(f"/person/{personId}", "?language=en-US")
    
    person_name = person_data.get("name", "Artista Desconhecido")
    
    movie_data = get_json("/search/movie", f"?query={person_name}&language=en-US")

    results = movie_data.get("results", [])

    filmes = []

    for movie in results:
        filmes.append({
            "title": movie.get("title", "Título Desconhecido"),
            "rank": movie.get("popularity", 0)
        })

    filmes.sort(reverse=True, key=lambda movie: movie["rank"])

    return {
        "person_id": personId,
        "person_name": person_name,
        "filmes": filmes
    }
    
@app.get("/filmes")
async def filmes_populares(limit=3):
    """ Obtem os filmes mais populares usando endpoint discover """
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({
            "title": movie['original_title'],
            "image":
                f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
            "id": movie['id']
        })
    return filtro

@app.get("/artistas/{id}")
async def artistas(id: int):
    
    data = get_json(
        "/person/",
        f"{id}?"
    )
    artista = {
            "nome": data['name'],
            "biografia": data['biography'],
            "imagem":
                f"https://image.tmdb.org/t/p/w185{data['profile_path']}"
        }
    
    
    return data

@app.post("/fav_artista/", response_model=schemas.Artistas)
async def favoritar_filme(artistas: schemas.Artistas, db: Session = Depends(get_db)):
    return crud.artistas(db=db, artistas=artistas)
    
@app.get("/fav_artista/", response_model=list[schemas.Artistas])
async def busca_artistas(db: Session = Depends(get_db)):
    return crud.busca_artistas(db)

@app.delete("/fav_artista/{tmdb_id}", response_model=schemas.Artistas)
async def delete_artista(tmdb_id: str, db: Session = Depends(get_db)):
    #db_favoritos = crud.get_favorito_by_tmdb_id (db, tmdb_id)
    #if db_favoritos is None:
        #raise HTTPException(status_code=404, detail="User not found")
    
    deleted_favorito=crud.delete_artista(db, tmdb_id)
    return deleted_favorito


if __name__ == "__main__":
    uvicorn.run("pycine:app", host="127.0.0.1", port=8000, reload=True)