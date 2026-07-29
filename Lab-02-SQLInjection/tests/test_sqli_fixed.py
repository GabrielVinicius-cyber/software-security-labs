def test_login_valido_funciona(client):
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'admin123'
    })

    assert response.status_code == 200
    assert response.get_json()['status'] == 'sucesso'


def test_login_invalido_e_rejeitado(client):
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'senhaerrada'
    })

    assert response.status_code == 401


def test_sqli_or_bypass_falha(client):
    response = client.post('/login', data={
        'username': "admin' OR '1'='1",
        'password': 'qualquercoisa'
    })

    assert response.status_code == 401
    assert response.get_json()['status'] == 'erro'


def test_sqli_comment_bypass_falha(client):
    response = client.post('/login', data={
        'username': "admin'--",
        'password': 'qualquercoisa'
    })

    assert response.status_code == 401
    assert response.get_json()['status'] == 'erro'
