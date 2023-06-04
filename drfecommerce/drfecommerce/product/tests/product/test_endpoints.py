"""
Test Endpoints
"""
import json
import factory
import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestCategoryEndPoints:
    endpoint = "/api/category/"

    def test_category_get(
        self, category_factory: factory.django.DjangoModelFactory, api_client: APIClient
    ):
        # Arrange
        category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestBrandEndPoints:
    endpoint = "/api/brand/"

    def test_brand_get(
        self, brand_factory: factory.django.DjangoModelFactory, api_client: APIClient
    ):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestProductEndPoints:
    endpoint = "/api/product/"

    def test_product_get(
        self, product_factory: factory.django.DjangoModelFactory, api_client: APIClient
    ):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4
