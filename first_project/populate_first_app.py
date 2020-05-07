import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'first_project.settings')

############################## ^^^ Point to environment settings? in Django ############################################

import django
django.setup()

############################## ^^^ Initiate Django ###########
import random

from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

## Initiate Faker module

faker_generator = Faker()

topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_Topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for entry in range(N):

        #get topic
        top = add_Topic()

        #Create Fake Topic
        fake_url = faker_generator.url()
        fake_date = faker_generator.date()
        fake_name = faker_generator.company()


        #Create Webpage entry
        web_page = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]


        # Create fake access record entry
        acc_rec = AccessRecord.objects.get_or_create(name=web_page, date=fake_date)[0]

if __name__ == "__main__":
    print("populating script...")
    populate(20)
    print("Populating Complete.")
