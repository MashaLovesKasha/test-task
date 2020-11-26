import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def email_validation(email):
    return bool(EMAIL_REGEX.match(email))
