from django.test import Client
import pytest


@pytest.fixture
def client():
    client = Client()
    return client


# company test

# list
@pytest.mark.django_db
def test_company_list_unauthorized(client):
    response = client.get('/company/', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_list(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/company/', follow=True)
    assert response.status_code == 200


# view
@pytest.mark.django_db
def test_company_view_unauthorized(client):
    response = client.get('/company/view/testowa', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_view(client):
    client.login(username='bartek', password='bartek')
    response = client.get('/company/view/testowa', follow=True)
    assert response.status_code == 200


# create
@pytest.mark.django_db
def test_company_create_unauthorized(client):
    response = client.post('/company/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_create(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/company/create/',
                           {'first_name': 'bartek', 'last_name': 'testowy', 'company': 'testowa', 'vehicle': 1},
                           follow=True)
    assert response.status_code == 200


# delete
@pytest.mark.django_db
def test_company_delete_unauthorized(client):
    response = client.post('/company/delete/testowa', follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_delete(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/company/delete/testowa', follow=True)
    assert response.status_code == 200


# edit
@pytest.mark.django_db
def test_company_edit_unauthorized(client):
    response = client.post('/company/edit/testowa', {'first_name': 'bartek'}, follow=False)
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_edit(client):
    client.login(username='bartek', password='bartek')
    response = client.post('/company/edit/testowa', {'first_name': 'bartek'}, follow=True)
    assert response.status_code == 200