"""file for s3 steps"""

from pytest_bdd import scenario, given, when, then, parsers
import src.S3
from pytest import fixture


@fixture
def s3_context(s3_setup_client):
    obj = src.S3.s3_obj()
    yield obj
    obj.cleanup_location(s3_setup_client)

@scenario('s3.feature', 'Can read file')
def test_can_read_file():
    pass

@given(parsers.parse('there is a file in {location}'))
def there_is_a_file_in_bucket_location(s3_context, s3_setup_client, location):
    s3_context.set_location(location)
    if s3_context.is_file_in_location(s3_setup_client):
        print("file exists not uploading")
    else:
        s3_context.upload_file(s3_setup_client)
    assert s3_context.get_error is not None

@when(parsers.parse('I try and read the file'))
def i_try_and_read_the_file(s3_context, s3_test_client):
    s3_context.read_file(s3_test_client)

@then('I don\'t get an S3 error')
def i_dont_get_an_s3_error(s3_context):
    err = s3_context.get_error()
    assert err is None
