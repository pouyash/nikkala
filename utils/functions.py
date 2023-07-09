from datetime import datetime

from django.utils.crypto import get_random_string


def create_activation_code():
    return str(get_random_string(length=72)) + str(datetime.now().microsecond)


