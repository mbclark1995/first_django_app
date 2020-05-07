import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django

django.setup()

from first_app.models import User
from faker import Faker

fake = Faker()

def populate(N = 5):
    for entry in range(N):

        fake_email = fake.email()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()

        user_list = User.objects.get_or_create(email_address = fake_email, first_name=fake_first_name, last_name=fake_last_name)[0]

if __name__ == "__main__":
    print("populating script...")
    populate(20)
    print("Populating Complete.")