import json
from fastapi import FastAPI
from datetime import datetime
from datetime import date
import pytz

#if _name_ == "_main_":
 #   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

app = FastAPI()

# app é o framework fastapi
# define uma rota ou endpoint, /hora
# GET 
@app.get("/hora") 
def horacerta():
    return {
        "hora": datetime.now(),
        "local": "BR"
    }

@app.get("/upper/{nome}") # <== endpoint
def upper(nome):
    return {
        "nome": nome,
        "upper": nome.upper()
    }

#Exercício 1
@app.get("/numero/{num}") 
def numero(num):
    resp = "impar"
    
    if int (num)%2 == 0:
        resp = "par"
    return {
        "numero": num,
        "tipo" : resp
    }

#Exercício 2
@app.get("/hora/{cidade}")
def hora(cidade):
    timezone = None
    
    if cidade == "tokyo":
        timezone = pytz.timezone("Asia/Tokyo")
    elif cidade == "london":
        timezone = pytz.timezone("Europe/London")
    else:
        timezone = pytz.timezone("America/Brasilia")

    return {
        "hora": datetime.now(timezone),
        "local": cidade
    }

#Exercício 3
@app.get("/diasemana")
def dia():
    resposta = date.today().weekday()
    dia = {0: "Segunda-Feira", 1: "Terça-Feira", 2: "Quarta-Feira", 3: "Quinta-Feira", 4: "Sexta-Feira", 5: "Sábado", 6: "Domingo"}

    return {
        "dia": dia[resposta]
    }
    
# retorna um livro de acordo com o id
# exemplo endpoint: 
# /book/2
@app.get("/book/{id}")
def get_book(id: int):
    with open("books.json") as f:
        data = json.load(f)
        # print(type(data))
        # print(data)
        for item in data:
            if item['id'] == id:
                return item  
    return {"error": f"book {id} not found"}  

# 2.Busca por ano    
@app.get("/book_ano/{ano}")
def get_book_ano(ano: int):
    with open("books.json", "r") as f:
        data = json.load(f)  
    books_of_year = []
    for item in data:
        if item['year'] == ano:
            books_of_year.append(item)
    if books_of_year:
        return books_of_year
    else:
        return {"error": f"No books found for the year {ano}"}

# 3.Busca por título
@app.get("/book_titulo/{titulo}")
def get_book_titulo(titulo):
    with open("books.json", "r") as f:
        data = json.load(f)  
    books_of_title = []
    for item in data:
        if titulo in item['title']:
            books_of_title.append(item)
    if books_of_title:
        return books_of_title
    else:
        return {"error": f"No books found for the year {titulo}"}

# 4.Busca por autor
@app.get("/book_autor/{autor}")
def get_book_autor(autor):
    with open("books.json") as f:
        data = json.load(f)  
    books_of_autor = []
    for item in data :
        for name in item['authors']:
            if autor.lower() in name.lower():
                books_of_autor.append(item)
    if books_of_autor:
        return books_of_autor
    else:
        return {"error": f"No books found for the year {autor}"}


# Criar o endpoint que realiza a ação:
# Exercício 1 - retornar JSON indicando se o número é
# "PAR" ou "IMPAR"

# Exercício 2 - informar 3 horários, de acordo com
# Brasília, Tóquio, Londres
# GET localhost:8000/hora/tokyo

# Exercício 3 - Dia da semana (segunda, terça, ...)

# iniciar o servidor web:
# uvicorn main:app --reload 
# print(horacerta())
