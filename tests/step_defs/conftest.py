""" Shared test file"""
from pytest import fixture
from pytest_bdd import given, parsers
from src.session import session as boto3
from botocore.config import Config
@fixture
def test_session():
    session = boto3()
    yield session

@fixture
def setup_session():
    session = boto3()
    session.create_session(profile_name= "setup")
    yield session

REGION = "eu-west-2"

@fixture
def s3_setup_client(setup_session):
    yield setup_session.get_session().client('s3')

@fixture
def s3_test_client(test_session):
    yield test_session.get_session().client('s3')

@fixture
def lambda_test_client(test_session):
    yield test_session.get_session().client('lambda', config=Config(region_name = REGION))

@given(parsers.parse('I am logged in as {profile_name:l}'))
def i_am_am_logged_in(test_session, profile_name):
    test_session.create_session(profile_name = profile_name)
