from django_seed import Seed
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

seeder = Seed.seeder()

from AppTwo.models import User
seeder.add_entity(User, 15)


if __name__ == '__main__':
    print('Creating user(s)...')
    inserted_pks = seeder.execute()
    print('User(s) created!')