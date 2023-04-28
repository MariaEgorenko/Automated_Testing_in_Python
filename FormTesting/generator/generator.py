from faker import Faker
from random import randint, sample

SUBJECTS = ('Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce', 'Economics'
            'Arts', 'Accounting', 'Social Studies', 'History', 'Civics')
faker = Faker()


class GeneratorPerson:
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    current_address = faker.address()
    date_of_birth = faker.date_between().strftime('%d %b %Y')
    mobile = faker.msisdn()
    subjects = sample(SUBJECTS, randint(1, len(SUBJECTS)))
