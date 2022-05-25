import pytest
from django.urls import reverse

from malves.django_assertions import assert_contains


@pytest.fixture
def resp_dashboard(client_com_usuario_logado, db):
    resp_dashboard = client_com_usuario_logado.get(reverse('dashboard:dashboard'), follow=True)
    return resp_dashboard


def test_status_code(resp_dashboard):
    assert resp_dashboard.status_code == 200


def test_title_dashboard(resp_dashboard):
    assert_contains(resp_dashboard, '<title> Ae Malves - Dashboard </title>')


def test_logout_link(resp_dashboard):
    assert_contains(resp_dashboard, '<p class="preview-subject mb-1">Log out</p>')
