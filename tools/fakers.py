import time


def generate_fake_email():
    return f'test.{time.time()}@gmail.com'


print(generate_fake_email())