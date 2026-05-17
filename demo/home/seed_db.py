from home.models import *
from faker import Faker

fake = Faker('en_IN')

def dbSeeder(records = 10) -> None:
    # college_names = ['IIT delhi', 'SRM University', 'BITS Pilani', 'IIT Bombay', 'IIT Madras']
    # for college in college_names:
    #     address = Faker().address()
    #     college_obj = College(college_name=college, college_address=address)
    #     college_obj.save()

    colleges = College.objects.all()
    for _ in range(records):
        college = fake.random_element(colleges)
        
        # Do something with the selected college, e.g., create a student associated with it
        name = fake.name()
        email = fake.email()
        mobile = fake.phone_number()
        age = fake.random_int(min=18, max=30)
        gender = fake.random_element(gender_choices)[0]
        Student.objects.create(
            name=name,
            email=email,
            gender=gender,
            age=age,
            college=college
        )