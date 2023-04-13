import pytest
from django import test

from {{ cookiecutter.project_slug }}.users.models import User
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def auth_user_client(user):
    client = test.Client()
    client.force_login(user)
    return client


@pytest.fixture
def unauth_user_client(user):
    client = test.Client()
    return client