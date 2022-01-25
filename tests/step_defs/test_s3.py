"""file for s3 steps"""

from pytest_bdd import scenario, given, when, then, parsers
import src.S3
from pytest import fixture


@fixture
def s3_context():
    obj = src.S3.s3_obj()
    yield obj
    obj.cleanup_location()

@scenario('s3.feature', 'Can read file')
def test_can_read_file():
    pass

@given(parsers.parse('there is a file in {location}'))
def there_is_a_file_in_bucket_location(s3_context, location):
    s3_context.set_location(location)
    if s3_context.is_file_in_location():
        print("file exists not uploading")
    else:
        s3_context.upload_file()
    assert True

@when(parsers.parse('I try and read the file'))
def i_try_and_read_the_file(s3_context):
    s3_context.read_file()

@then('I don\'t get an error')
def then_i_dont_get_an_error():
    assert True
