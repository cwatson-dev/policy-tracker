from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

import re

class PasswordUpperCharacterValidator(object):

    def validate(self, password, user=None):
        if not any(c.isupper() for c in password):
            raise ValidationError(
                _("This password must contain at least 1 uppercase character."),
                code='password_no_uppercase',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase character."
        )

class PasswordLowerCharacterValidator(object):

    def validate(self, password, user=None):
        if not any(c.islower() for c in password):
            raise ValidationError(
                _("This password must contain at least 1 lowercase character."),
                code='password_no_lowercase',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase character."
        )

class PasswordOneNumberValidator(object):

    def validate(self, password, user=None):
        if not any(c.isdigit() for c in password):
            raise ValidationError(
                _("This password must contain at least 1 number."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 number."
        )

class PasswordSpecialCharacterValidator(object):

    def validate(self, password, user=None):
        if not set('[~!@#$%^&*()_-+={}":;\']+$').intersection(password):
            raise ValidationError(
                _("This password must contain at least 1 special character (~!@#$%^&*()_-+={}\"-:;'[])."),
                code='password_no_special_character',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character (~!@#$%^&*()_+={}\"-:;'[])."
        )

class PasswordConsecutivesValidator(object):

    def validate(self, password, user=None):
        if re.search(r'(.)\1', password):
            raise ValidationError(
                _("This password cannot contain any consecutive characters."),
                code='password_consecutives',
            )

    def get_help_text(self):
        return _(
            "Your password cannot contain any consecutive characters."
        )
