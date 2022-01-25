""" Shared test file"""
from pytest import fixture
from pytest_bdd import given
from src.session import session as boto3
@fixture
def session():
    session = boto3()
    yield session

@fixture
def sts_client(session):
    yield session.get_session().client('sts')

@given('I am logged in')
def i_am_am_logged_in(sts_client):
    print(sts_client.get_caller_identity())
