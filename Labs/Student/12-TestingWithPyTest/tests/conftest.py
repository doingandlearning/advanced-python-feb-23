from project.models import User
from project import create_app
import pytest

@pytest.fixture(scope="module")
def new_user():
	user = User("kevin@cool.com", "FlaskIsAwesome")
	return user

# function
# class
# session

@pytest.fixture(scope="module")
def test_client():
	flask_app = create_app('flask_test.cfg')
	with flask_app.test_client() as test_client:
		with flask_app.app_context():
			yield test_client