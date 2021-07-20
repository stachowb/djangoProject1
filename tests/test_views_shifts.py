from django.test import Client
import pytest


@pytest.fixture
def client():
    client = Client()
    return client


# shifts test

# list
@pytest.mark.django_db
def test_shift_list_unauthorized(client):
    response = client.get('/shift/', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_shift_list(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/shift/', follow=True)
    assert response.status_code == 200


# view
@pytest.mark.django_db
def test_shift_view_unauthorized(client):
    response = client.get('/shift/view/19-07-2021-1200-19-07-2021-2100', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_shift_view(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/shift/view/19-07-2021-1200-19-07-2021-2100', follow=True)
    assert response.status_code == 200


# create
@pytest.mark.django_db
def test_shift_create_unauthorized(client):
    response = client.post('/shift/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_shift_create(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/shift/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=True)
    assert response.status_code == 200


# delete
@pytest.mark.django_db
def test_shift_delete_unauthorized(client):
    response = client.post('/shift/delete/19-07-2021-1200-19-07-2021-2100', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_shift_delete(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/shift/delete/19-07-2021-1200-19-07-2021-2100', follow=True)
    assert response.status_code == 200


# edit
@pytest.mark.django_db
def test_shift_edit_unauthorized(client):
    response = client.post('/shift/edit/19-07-2021-1200-19-07-2021-2100', {'first_name': 'bartek'}, follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_shift_edit(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/shift/edit/19-07-2021-1200-19-07-2021-2100', {'first_name': 'bartek'}, follow=True)
    assert response.status_code == 200
