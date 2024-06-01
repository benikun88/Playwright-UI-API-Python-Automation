import json

import allure
import pytest
from http import HTTPStatus
from configs.config_API import base_url, common_headers, random_email, customer_payload, login_payload, \
    login_payload_negative, register_payload_wrong_password_rules, register_password_roles_error, register_payload
from answers.api_calls import ApiRequests


@pytest.mark.xdist_group(name="serial")
@allure.feature("API Tests")
@allure.story("Login API test")
@pytest.mark.api
class TestApi:
    @pytest.fixture
    def customer_token(self):
        url = f"{base_url}/users/login"
        response = ApiRequests.post(url, json=login_payload, headers=common_headers)
        assert response.status_code == HTTPStatus.OK, f"Failed to create customer token: {response.text}"
        print(response.json()["access_token"])
        return response.json()["access_token"]

    @allure.description("Test login with existing user")
    def test_login(self):
        url = f"{base_url}/users/login"
        response = ApiRequests.post(url, json=login_payload, headers=common_headers)
        assert response.status_code == HTTPStatus.OK, f"error: {response.text}"
        access_token_id = response.json()["access_token"]
        print(response.json()["access_token"])
        assert access_token_id is not None, "Customer ID not received"

    @allure.description("Test login with existing user")
    def test_login_wrong_cred(self):
        url = f"{base_url}/users/login"
        response = ApiRequests.post(url, json=login_payload_negative, headers=common_headers)
        print(response.json())
        assert response.status_code == HTTPStatus.UNAUTHORIZED, f"Failed to create customer: {response.text}"

    @allure.description("Test logout with existing user")
    def test_logout(self, customer_token):
        url = f"{base_url}/users/logout"
        headers = {
            **common_headers,
            "Authorization": f"Bearer {customer_token}",
        }
        print(json.dumps(headers, indent=4))
        response = ApiRequests.get(url, json=json, headers=headers)
        print(response.json())
        message = response.json()
        assert response.status_code == HTTPStatus.OK, f"Failed to create customer: {response.text}"
        assert message["message"] == "Successfully logged out", "Unauthorized"

    @allure.description("Test register with wrong data")
    def test_wrong_password_rules_register(self):
        url = f"{base_url}/users/register"
        response = ApiRequests.post(url, json=register_payload_wrong_password_rules, headers=common_headers)
        print(response.json())
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, f"Failed to create customer: {response.text}"
        assert response.json()["password"] == register_password_roles_error, f"Failed to create customer: {response.text}"

    @allure.description("Test register with correct data")
    def test_new_user_register(self):
        url = f"{base_url}/users/register"
        response = ApiRequests.post(url, json=register_payload, headers=common_headers)
        print(response.json())
        assert response.status_code == HTTPStatus.CREATED, f"Failed to create customer: {response.text}"
        assert response.json()["id"] is not None, f"Failed to create customer: {response.text}"
