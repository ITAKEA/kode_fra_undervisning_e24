import random
from faker import Faker

# object af Faker
fake = Faker() # https://faker.readthedocs.io/en/stable/

# Funktion der returnerer en random dictionary med en user
def create_random_user():
    return {
        "id": random.randint(1, 1000),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"),
        "gender": random.choice(["Male", "Female"]),
        "email": fake.email(),
        "phonenumber": fake.phone_number(),
        "address": fake.address(),
        "nationality": fake.country(),
        "active": random.choice([True, False]),
        "github_username": fake.user_name()
    }

# List comprehension der genererer en liste med 10 random_user dictionaries
random_users = [create_random_user() for _ in range(10)]


# random_users kan alternativt laves med et for loop
"""
random_users = []
for _ in range(10):
  random_users.append(create_random_user())
"""

# Se denne video om List Comprehension : https://www.youtube.com/watch?v=AhSvKGTh28Q
# Eller brug denne prompt: https://itakea.github.io/e24_swa/auditional_exercises.html#list-comprehensions