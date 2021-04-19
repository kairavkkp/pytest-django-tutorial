from django.test import TestCase
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test_user', 'test@kkp.com', 'password')
    assert User.objects.count() == 1
