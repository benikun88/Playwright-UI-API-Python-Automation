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
class TestCartApi:
    def test_create_cart(self):
        url = f"{base_url}/carts"
        response = ApiRequests.post(url, json=None, headers=common_headers)
        assert response.status_code == HTTPStatus.CREATED, f"Failed to create customer token: {response.text}"
        assert response.json()["id"] is not None, "Customer ID not received"

    @allure.description("Test login with existing user")
    def test_login(self):
        url = f"{base_url}/users/login"
        response = ApiRequests.post(url, json=login_payload, headers=common_headers)
        assert response.status_code == HTTPStatus.OK, f"error: {response.text}"
        access_token_id = response.json()["access_token"]
        print(response.json()["access_token"])
        assert access_token_id is not None, "Customer ID not received"