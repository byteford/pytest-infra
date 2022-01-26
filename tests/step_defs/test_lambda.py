"""file for lambda steps"""

from pytest_bdd import scenario, given, when, then, parsers
from src.aws_lambda import lambda_obj
from pytest import fixture

@fixture
def lambda_context(s3_setup_client):
    obj = lambda_obj()
    yield obj

@scenario('lambda.feature', 'Can run lambda')
def test_can_run_lambda():
    pass

@when(parsers.parse('I run {name} lambda'))
def i_run_a_lambda(name, lambda_context, lambda_test_client):
    lambda_context.run_lambda(name, lambda_test_client)

@then('The lambda will pass')
def the_lambda_will_pass(lambda_context):
    err = lambda_context.get_error()
    assert err is None