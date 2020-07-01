import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')
import django
django.setup()
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker
fake_gen=Faker()
topics=['Search','Social','News','Games']
def add_top():

    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N):
    for entry in range(N):
        top=add_top()
        fake_url=fake_gen.url()
        fake_date=fake_gen.date()
        fake_name=fake_gen.company()
        Webpg=Webpage.objects.get_or_create(Topic=top,url=fake_url,name=fake_name)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=Webpg,date=fake_date)[0]
if __name__ == '__main__':
    print("populating Script")

    populate(20)
    print("population compleated")
