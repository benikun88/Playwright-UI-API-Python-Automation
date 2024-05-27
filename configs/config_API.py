# config_API.py
import uuid
from utilities.helper import HelperCommon
helper = HelperCommon()
random_email = helper.generate_random_email()

# Credentials
consumer_key = "u5gkmvsnxvc5w6qxoy2iwx98mkc1j30d"
consumer_secret = "brpz2fvopf9fcdlkqh6dlbh8ui5lqow6"
access_token = "55yrut70u8qgvkvaw7xc9yvokhs09ztw"
access_token_secret = "64ueg9agxzzy4pgsxd73qqnj7f36lkom"

# Base URL
base_url = "https://api.practicesoftwaretesting.com"

# Common headers
common_headers = {
    "Content-Type": "application/json",
    "Host": "api.practicesoftwaretesting.com",
    # "Content-Length": "69",
    # "Cookie": "PHPSESSID=827611b7d87be75f321673ab0c102a07",
    "User-Agent": "Chrome/111.0.5575.46"
}

# Generate random email
random_email = f"jdoe{uuid.uuid4().hex[:6]}@example.com"

# Create customer payload
customer_payload = {
    "customer": {
        "email": random_email,
        "firstname": "Jane",
        "lastname": "Doe",
        "addresses": [{
            "defaultShipping": True,
            "defaultBilling": True,
            "firstname": "Jane",
            "lastname": "Doe",
            "region": {
                "regionCode": "NY",
                "region": "New York",
                "regionId": 43
            },
            "postcode": "10755",
            "street": ["123 Oak Ave"],
            "city": "Purchase",
            "telephone": "512-555-1111",
            "countryId": "US"
        }]
    },
    "password": "Password1"
}

login_payload = {
    "email": "admin@practicesoftwaretesting.com",
    "password": "welcome01"
}
login_payload_negative = {
    "email": "admin@practicesoftwaretesting.com",
    "password": "welcome011"
}
register_payload_wrong_password_rules = {
  "first_name": "John",
  "last_name": "Doe",
  "address": "Street 1",
  "city": "City",
  "state": "State",
  "country": "Country",
  "postcode": "1234AA",
  "phone": "0987654321",
  "dob": "1970-01-01",
  "password": "s",
  "email": "john1@doe.example"
}
register_payload = {
  "first_name": "benjamin",
  "last_name": "Kun",
  "address": "Street 1",
  "city": "City",
  "state": "State",
  "country": "Country",
  "postcode": "1234AA",
  "phone": "0987654321",
  "dob": "1970-01-01",
  "password": "Orvagas1992!",
  "email":random_email
}
register_password_roles_error=[
            "The password field must be at least 8 characters.",
            "The password field must contain at least one uppercase and one lowercase letter.",
            "The password field must contain at least one symbol.",
            "The password field must contain at least one number."
        ]
