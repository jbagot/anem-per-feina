import datetime
import random

import factory
from factory import fuzzy
from faker import Faker

from accounts.models import User
from jobsapp.models import NO_REMOTE, PARTIAL_REMOTE, REMOTE, Job

faker = Faker("es_ES")

# List of factories
class UserFactory(factory.django.DjangoModelFactory):  # type: ignore
    class Meta:
        model = User
        django_get_or_create = ("first_name", "last_name")

    first_name = factory.Faker("first_name", locale="es_ES")
    last_name = "Doe"
    email = factory.Faker("email", locale="es_ES")


class JobFactory(factory.django.DjangoModelFactory):  # type: ignore
    class Meta:
        model = Job

    user = factory.SubFactory("tests.factories.UserFactory")
    title = factory.Sequence(lambda n: f"Title {n}")
    location = factory.Faker("address", locale="es_ES")
    company_name = factory.Faker("company", locale="es_ES")
    company_description = factory.Faker("text", locale="es_ES")
    description = factory.Sequence(lambda n: f"Description {n}")
    last_date = datetime.datetime.now() + datetime.timedelta(days=10)
    website = factory.Faker("url", locale="es_ES")
    type = "1"
    category = fuzzy.FuzzyChoice(["Senior", "Junior", "Manager"])
    remote = fuzzy.FuzzyChoice([REMOTE, NO_REMOTE, PARTIAL_REMOTE])
