import requests
import copy

from requests.exceptions import HTTPError


def build_dict_id_people(people):
    id_to_people = {}
    for p in people:
        if "films" in p:
            for id in p["films"]:
                if id in id_to_people:
                    id_to_people[id].append(p["name"])
                else:
                    id_to_people[id] = [p["name"]]
    return id_to_people


def get_id_people_mapping(all_people):
    people = copy.deepcopy(all_people)
    for p in people:
        if "films" in p:
            p["films"] = list(map(lambda x: x.split("/")[-1], p["films"]))
    filmId_to_people = build_dict_id_people(people)
    return filmId_to_people


def get_people():
    people = None
    try:
        response = requests.get("https://ghibliapi.herokuapp.com/people")
        response.raise_for_status()
    except HTTPError as he:
        print("HTTP error: {he}")
    except Exception as e:
        print(f"An error occured: {e}")
    else:
        people = response.json()
    return people
