import pytest
from django.urls import reverse

from malves.django_assertions import assert_contains


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'), follow=True)
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Ae Malves - Home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">AE MALVES</a>')
