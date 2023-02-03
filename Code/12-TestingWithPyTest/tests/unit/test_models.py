
def test_new_user_has_correct_details_after_init(new_user):
	# Arrange  GIVEN  a User model
	# Act   	 WHEN create a new user with known email and password
	# Assert   THEN the email will and the password witll be different
	assert new_user.email == 'kevin@cool.com'
	assert new_user.password_hashed != 'FlaskIsAwesome'

def test_new_user_has_a_role_of_user(new_user):
	assert new_user.role == "user"
	assert new_user.role != "admin"

