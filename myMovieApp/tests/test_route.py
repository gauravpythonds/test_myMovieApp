
def test_route_movies(app, client):
    response = client.get('/movies/')
    assert response.status_code == 200
