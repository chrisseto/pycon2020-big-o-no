import pytest

@pytest.fixture(scope='session')
def django_db_createdb():
    return False

@pytest.fixture(scope='session')
def django_db_keepdb():
    return True

@pytest.fixture(scope='session')
def django_db_use_migrations():
    return False
