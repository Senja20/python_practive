import random

from faker import Faker


fake = Faker()


def student_to_string(s):
    return f'id: {s["id"]}, name: {s["name"]}, email: {s["email"]}, year: {s["year"]}'


def get_student(id=0):
    name = fake.name()

    return {
        'id': id,
        'name': name,
        'email': '.'.join(name.lower().split()) + '@' + fake.free_email_domain(),
        'year': random.randint(2000, 2019)
    }


def get_course(id=0):
    name = fake.sentence(nb_words=2)
    return {
        'id': id,
        'name': name,
        'max_students': random.randint(10, 100) * 5
    }


def get_test(id=0, course_id=0):
    name = fake.sentence(nb_words=2)
    return {
        'id': id,
        'course_id': course_id,
        'name': name,
        'date_time': str(fake.date_time_between(start_date='+1w', end_date='+12m'))
    }


def get_posts():
    post_count = random.randrange(30, 50)

    posts = []
    for i in range(post_count):
        post = {
            'id': str(i + 1),
            'userId': str(random.randrange(1, 100)),
            'title': fake.sentence(nb_words=4).title(),
            'body': fake.sentence(nb_words=8).capitalize() + '.'
        }

        posts.append(post)

    return posts
