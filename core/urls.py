from django.contrib import admin
from django.urls import path

from courses.views import all_courses

urlpatterns = [
    path("courses/", all_courses),
    path("admin/", admin.site.urls),
]
