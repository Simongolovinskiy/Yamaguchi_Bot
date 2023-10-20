import random
import string


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(8, 15)))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def generate_random_name():
    first_names = ["Василий", "Евгений", "Алиса", "Геннадий", "Алексей", "Александр"]
    last_names = ["Пупкин", "Гнилозубов", "Тьюринг", "Дробышев", "Столяров", "Кузнецов"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    return f"{first_name} {last_name}"
