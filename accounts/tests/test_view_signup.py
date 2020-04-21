from django.contrib.auth.models import User
from django.urls import resolve, reverse
from django.test import TestCase

from ..views import signup
from ..form import SignUpForm


class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)