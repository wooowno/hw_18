from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.model.movie import MovieSchema

movie_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        if did := request.args.get("director_id"):
            movies = movie_service.get_by_director(did)
        elif gid := request.args.get("genre_id"):
            movies = movie_service.get_by_genre(gid)
        elif year := request.args.get("year"):
            movies = movie_service.get_by_year(year)
        else:
            movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)

        return "", 201


@movie_ns.route("/<int:mid>")
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)

        return "", 204

    def patch(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)

        return "", 204
