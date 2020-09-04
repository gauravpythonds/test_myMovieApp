from myMovieApp import people_helper

data_test = [
    {
        "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
        "name": "Pazu",
        "age": "13",
        "films": [
            "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/fe93adf2-2f3a-4ec4-9f68-5422f1b87c01"
    },
    {
        "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
        "name": "Lusheeta Toel Ul Laputa",
        "age": "13",
        "films": [
            "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/598f7048-74ff-41e0-92ef-87dc1ad980a9"
    },
    {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Ashitaka",
        "age": "late teens",
        "films": [
            "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"
    }
]

def test_get_id_people_mapping():
    result = people_helper.get_id_people_mapping(data_test)
    assert result == {
        "2baf70d1-42bb-4437-b551-e5fed5a87abe" : ["Pazu", "Lusheeta Toel Ul Laputa"],
        "0440483e-ca0e-4120-8c50-4c8cd9b965d6" : ["Ashitaka"]
    }

def test_get_id_people_mapping_empty():
    result = people_helper.get_id_people_mapping([])
    assert result == {}


