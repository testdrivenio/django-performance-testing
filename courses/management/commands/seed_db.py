from django.core.management.base import BaseCommand
from faker import Faker

from courses.models import Author, Course


class Command(BaseCommand):
    help = "Seeds the database with 10 authors and 100 courses"

    def handle(self, *args, **options):
        fake = Faker()

        # remove existing data
        Author.objects.all().delete()
        Course.objects.all().delete()

        # add 10 authors
        authors = [Author(name=fake.name()) for index in range(10)]
        Author.objects.bulk_create(authors)
        print(f"Authors created.")

        # add 100 courses
        courses = []
        for author in Author.objects.all():
            for _ in range(10):
                course_title = fake.sentence(nb_words=4)
                course = Course(title=course_title, author=author)
                courses.append(course)
        Course.objects.bulk_create(courses)
        print(f"Courses created.")
