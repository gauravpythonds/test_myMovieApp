import requests
import copy
from requests.exceptions import HTTPError

import people_helper


def get_all_movies():
    all_movies = None
    try:
        response = requests.get("https://ghibliapi.herokuapp.com/films")
        response.raise_for_status()
    except HTTPError as he:
        print("HTTP error: {he}")
    except Exception as e:
        print(f"An error occured: {e}")
    else:
        all_movies = response.json()
    return all_movies


def add_people_field(all_movies, all_people):
    movies_with_people = copy.deepcopy(all_movies)
    id_people_mapping = people_helper.get_id_people_mapping(all_people)
    for x in movies_with_people:
        x["people"] = id_people_mapping.get(x["id"], [])
    return movies_with_people
