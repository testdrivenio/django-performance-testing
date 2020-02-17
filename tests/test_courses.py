import json

import pytest
from faker import Faker

# from django.test import override_settings

from courses.models import Author, Course


@pytest.mark.django_db
# @override_settings(NPLUSONE_RAISE=True)
def test_number_of_sql_queries_all_courses(client, django_assert_num_queries):
    fake = Faker()

    author_name = fake.name()
    author = Author(name=author_name)
    author.save()
    course_title = fake.sentence(nb_words=4)
    course = Course(title=course_title, author=author)
    course.save()

    with django_assert_num_queries(1):
        res = client.get("/courses/")
        data = json.loads(res.content)

        assert res.status_code == 200
        assert len(data) == 1

        author_name = fake.name()
        author = Author(name=author_name)
        author.save()
        course_title = fake.sentence(nb_words=4)
        course = Course(title=course_title, author=author)
        course.save()

        res = client.get("/courses/")
        data = json.loads(res.content)

        assert res.status_code == 200
        assert len(data) == 2
