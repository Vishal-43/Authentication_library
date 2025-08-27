import secrets


def generate_otp():
    return secrets.randbelow(1000000)