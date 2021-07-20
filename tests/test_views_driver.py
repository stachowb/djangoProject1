from django.test import Client
import pytest


@pytest.fixture
def client():
    client = Client()
    return client


# driver tests

# list
@pytest.mark.django_db
def test_driver_list_unauthorized(client):
    response = client.get('/driver/', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_list(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/driver/', follow=True)
    assert response.status_code == 200


# view
@pytest.mark.django_db
def test_driver_view_unauthorized(client):
    response = client.get('/driver/view/bartek-stachow/', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_view(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/driver/view/bartek-stachow', follow=True)
    assert response.status_code == 200


# create
@pytest.mark.django_db
def test_driver_create_unauthorized(client):
    response = client.post('/driver/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_create(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/driver/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=True)
    assert response.status_code == 200


# delete
@pytest.mark.django_db
def test_driver_delete_unauthorized(client):
    response = client.post('/driver/delete/bartek-stachow/', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_delete(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/driver/delete/bartek-stachow', follow=True)
    assert response.status_code == 200


# edit
@pytest.mark.django_db
def test_driver_edit_unauthorized(client):
    response = client.post('/driver/edit/bartek-stachow/', {'first_name': 'bartek'}, follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_driver_edit(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/driver/edit/bartek-stachow', {'first_name': 'bartek'}, follow=True)
    assert response.status_code == 200



