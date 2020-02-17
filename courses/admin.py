from django.contrib import admin

from courses.models import Author, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
