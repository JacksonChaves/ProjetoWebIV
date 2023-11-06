from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    #SELECT * from users where id = user_id
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

def favoritar(db:Session, favorito: schemas.Favoritos):
    existing_favorito = get_tmdb_id(db, favorito.user_id, favorito.tmdb_id)
    if existing_favorito:
        raise HTTPException(status_code=400, detail="Movie already favorited by this user")
    db_favorito= models.Favorito_movie(tmdb_id=favorito.tmdb_id, user_id=favorito.user_id, title=favorito.title)
    db.add(db_favorito)
    db.commit()
    db.refresh(db_favorito)
    return db_favorito

def get_favorito_by_tmdb_id(db: Session, user_id: str):
    return db.query(models.Favorito_movie).filter_by(user_id=user_id).all()

def get_tmdb_id(db: Session, user_id: str, tmdb_id: str):
    return db.query(models.Favorito_movie).filter_by(user_id=user_id, tmdb_id=tmdb_id).all()

def delete_favorito(db: Session, tmdb_id: str):
    favorito = db.query(models.Favorito_movie).filter(models.Favorito_movie.tmdb_id == tmdb_id).first()
    db.delete(favorito)
    db.commit()
    return favorito