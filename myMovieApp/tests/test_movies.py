from myMovieApp import movies_helper

data_test_movies = [
    {
        "id": "ff24da26-a969-4f0e-ba1e-a122ead6c6e3",
        "title": "Whisper of the Heart",
        "people": [
            "https://ghibliapi.herokuapp.com/people/"
        ],
        "url": "https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3"
    },
    {
        "id": "45204234-adfd-45cb-a505-a8e7a676b114",
        "title": "My Neighbors the Yamadas",
        "people": [
            "https://ghibliapi.herokuapp.com/people/"
        ],
        "url": "https://ghibliapi.herokuapp.com/films/45204234-adfd-45cb-a505-a8e7a676b114"
    }
]

data_test_people = [
    {
        "id": "6b3facea-ea33-47b1-96ce-3fc737b119b8",
        "name": "Renaldo Moon aka Moon aka Muta",
        "films": [
            "https://ghibliapi.herokuapp.com/films/90b72513-afd4-4570-84de-a56c312fdf81",
        "https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3"
        ]
    },
    {
        "id": "fc196c4f-0201-4ed2-9add-c6403f7c4d32",
        "name": "Baron Humbert von Gikkingen",
        "films": [
            "https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3",
            "https://ghibliapi.herokuapp.com/films/90b72513-afd4-4570-84de-a56c312fdf81"
        ]
    }
]


expected_output = [
    {
        "id": "ff24da26-a969-4f0e-ba1e-a122ead6c6e3",
        "title": "Whisper of the Heart",
        "people": [
            "Renaldo Moon aka Moon aka Muta",
            "Baron Humbert von Gikkingen"
        ],
        "url": "https://ghibliapi.herokuapp.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3"
    },
    {
        "id": "45204234-adfd-45cb-a505-a8e7a676b114",
        "title": "My Neighbors the Yamadas",
        "people": [],
        "url": "https://ghibliapi.herokuapp.com/films/45204234-adfd-45cb-a505-a8e7a676b114"
    }
]


def test_add_people_field():
    result = movies_helper.add_people_field(data_test_movies, data_test_people)
    assert result == expected_output
