# import pytest
# from django.urls import reverse
#
# from malves.django_assertions import assert_contains
#
#
# @pytest.fixture
# def resp_dashboard(client, db):
#     resp_dashboard = client.get(reverse('dashboard:dashboard'), follow=True)
#     return resp_dashboard
#
#
# def test_status_code(resp_dashboard):
#     assert resp_dashboard.status_code == 200
