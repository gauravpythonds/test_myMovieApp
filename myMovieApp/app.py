import os

from flask_caching import Cache
from flask import jsonify
from flask import Flask, render_template

import movies_helper
import people_helper


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    config = {
        "DEBUG": True,
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 60
    }
    app.config.from_mapping(config)
    cache = Cache(app)

    @app.route("/movies/", methods=['GET'])
    @cache.cached(timeout=60)
    def get_movies_people():
        movies = movies_helper.get_all_movies()
        if movies is None:
            return "Error while fetching movies"
        all_people = people_helper.get_people()
        if all_people is None:
            return "Error while fetching people"
        movies_with_people = movies_helper.add_people_field(movies, all_people)
        return render_template('movies.html', films=movies_with_people)

    return app
