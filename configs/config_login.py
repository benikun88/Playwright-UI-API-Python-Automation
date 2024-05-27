# Test data
VALID_USERNAME = "customer@practicesoftwaretesting.com"
VALID_PASSWORD = "welcome01"

INVALID_USERNAME = "customer@practicesoftwaretesting.co"
EMPTY_PASSWORD = ""

# Expected error messages
EXPECTED_EMAIL_ERROR = "Please enter a valid email address (Ex: johndoe@domain.com)."
EXPECTED_PASSWORD_ERROR = "This is a required field."
EXPECTED_PASSWORD_SUCCESS = ("If there is an account associated with Benikun88@gmail.com you will receive an email "
                             "with a link to reset your password.")
EXPECTED_PASSWORD_TEXTBOX_ERROR = "Please enter a valid email address (Ex: johndoe@domain.com)."

# Expected success messages
EXPECTED_SUCCESS_LOGIN = "Welcome, Benjamin Kun!"
EXPECTED_SUCCESS_LOGOUT_MSG = "You are signed out"

# Test URLs
LOGIN_PAGE_URL = "https://example.com/login"

# Other configurations
WAIT_TIME = 10  # Adjust this according to your needs
TEST_DATA=[
        ("customer@practicesoftwaretesting.com", "welcome01", None),  # Valid credentials
        ("customer@practicesoftwaretesting.co", "welcome01", "Invalid email or password"),  # Wrong email
        ("customer@practicesoftwaretesting.com", "", "Password is required."),  # Empty password
        ("", "welcome01", "E-mail is required.")  # Empty email
    ]