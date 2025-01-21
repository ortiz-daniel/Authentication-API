import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from main import app
from src.database.models import engine, User, LoginSessions

client = TestClient(app)

def test_register_user():
    import uuid

    SQLModel.metadata.create_all(engine)

    response = client.post(
        '/users/',
        json={
            'email': f'{str(uuid.uuid4())}@test.com',
            'password': 'mockpassword'
        }
    )
    assert response.status_code == 201
    assert response.json()['message'] == 'Usuario creado con éxito'

def test_login_user():
    import uuid

    SQLModel.metadata.create_all(engine)

    email = f'{str(uuid.uuid4())}@test.com'
    password = 'mockpassword'

    response = client.post(
        '/users/',
        json={
            'email': email,
            'password': password
        }
    )
    assert response.status_code == 201

    response = client.post(
        '/auth/login',
        json={
            'email': email,
            'password': password
        }
    )

    assert response.status_code == 200
    assert 'token' in response.json()


def test_login_history():
    import uuid

    SQLModel.metadata.create_all(engine)

    email = f'{str(uuid.uuid4())}@test.com'
    password = 'mockpassword'

    response = client.post(
        '/users/',
        json={
            'email': email,
            'password': password
        }
    )
    assert response.status_code == 201

    response = client.post(
        '/auth/login',
        json={
            'email': email,
            'password': password
        }
    )

    assert response.status_code == 200
    assert 'token' in response.json()

    token = response.json()['token']

    response = client.get(
        '/users/sessions',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert 'history_sessions' in response.json()
    assert len(response.json()['history_sessions']) == 1