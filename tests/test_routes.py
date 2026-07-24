def test_index_route(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.get_json() == {"message": "Lab-01-Flask rodando com sucesso!"}


def test_status_route(client):
    response = client.get('/status')

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
