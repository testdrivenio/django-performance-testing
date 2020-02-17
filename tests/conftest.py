from django.conf import settings


def pytest_configure(config):
    settings.NPLUSONE_RAISE = True
