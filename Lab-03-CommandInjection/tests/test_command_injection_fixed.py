def test_ping_legitimo_funciona(client):
    response = client.get('/ping?host=127.0.0.1')

    assert response.status_code == 200
    assert response.get_json()['status'] == 'sucesso'
    assert 'bytes' in response.get_json()['output'] or 'PING' in response.get_json()['output']


def test_ping_sem_host_retorna_erro(client):
    response = client.get('/ping')

    assert response.status_code == 400


def test_injecao_semicolon_nao_executa_comando(client):
    response = client.get('/ping?host=127.0.0.1;whoami')

    data = response.get_json()
    assert 'kali' not in data['output']
    assert data['output'] == ''


def test_injecao_and_nao_executa_comando(client):
    response = client.get('/ping?host=127.0.0.1 && id')

    data = response.get_json()
    assert 'uid=' not in data['output']
    assert data['output'] == ''


def test_injecao_pipe_nao_executa_comando(client):
    response = client.get('/ping?host=127.0.0.1 | uname -a')

    data = response.get_json()
    assert 'Linux' not in data['output']
    assert data['output'] == ''
