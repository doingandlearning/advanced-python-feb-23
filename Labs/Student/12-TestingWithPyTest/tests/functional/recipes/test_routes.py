from project import create_app

def test_home_page(test_client):
	"""
	GIVEN a Flask app ready for testing
	WHEN the '/' is hit with a GET request
	THEN some known text will be returned with a 200 Status code
	"""
	response = test_client.get("/")
	assert response.status_code == 200
	assert b"Welcome to the" in response.data
	assert b"Need an account?" in response.data


def test_home_page_post(test_client):
	"""
	GIVEN a Flask app ready for testing
	WHEN the '/' is hit with a POST request
	THEN should fail with a non 200 status code
	"""
	response = test_client.post("/")
	assert response.status_code != 200
	assert response.status_code == 405