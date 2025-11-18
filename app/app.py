from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items_db = {}

counter_id = 1

class MovieCreate(BaseModel):
    title: str
    year: int
    genre: str

class MovieRead(BaseModel):
    id: int
    title: str
    year: int
    genre: str


@app.post("/movies/")
def create_movie(movie: MovieCreate) -> MovieRead:
    global counter_id
    movie_id = counter_id
    counter_id += 1
    movie_dict = {"id": movie_id, "title": movie.title, "year": movie.year, "genre": movie.genre}

    items_db[movie_id] = movie_dict

    return MovieRead(**movie_dict)

@app.get("/movies/")
def getsMovies() -> list[MovieRead]:
    movies = []
    for movie_dict in items_db.values():
        movies.append(MovieRead(**movie_dict))
    return movies

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: MovieCreate) -> MovieRead:
    if movie_id not in items_db:
        raise HTTPException(status_code=404, detail="Movie not found")

    movie_dict = {"id": movie_id, "title": movie.title, "year": movie.year, "genre": movie.genre}
    items_db[movie_id] = movie_dict

    return MovieRead(**movie_dict)

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int) -> dict:
    if movie_id not in items_db:
        raise HTTPException(status_code=404, detail="Movie not found")

    del items_db[movie_id]

    return {"detail": "Movie deleted successfully"}