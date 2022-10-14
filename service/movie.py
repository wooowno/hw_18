from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService


class MovieService:
    def __init__(self, dao: MovieDAO, genre_service: GenreService, director_service: DirectorService):
        self.dao = dao
        self.genre_service = genre_service
        self.director_service = director_service

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_director(self, did):
        return self.dao.get_by_director(did)

    def get_by_genre(self, gid):
        return self.dao.get_by_genre(gid)

    def get_by_year(self, year):
        return self.dao.get_by_year(year)

    def create(self, data):
        movie = Movie(**data)

        movie.genre = self.genre_service.get_one(movie.id)
        movie.director = self.director_service.get_one(movie.id)

        return self.dao.create(movie)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        movie.genre = self.genre_service.get_one(movie.id)
        movie.director = self.director_service.get_one(movie.id)

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        if "title" in data:
            movie.title = data.get("title")

        if "description" in data:
            movie.description = data.get("description")

        if "trailer" in data:
            movie.trailer = data.get("trailer")

        if "year" in data:
            movie.year = data.get("year")

        if "rating" in data:
            movie.rating = data.get("rating")

        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
            movie.genre = self.genre_service.get_one(movie.id)

        if "director_id" in data:
            movie.director_id = data.get("director_id")
            movie.director = self.director_service.get_one(movie.id)

        return self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
