from django.db import models
from loguru import logger


class Customer(models.Model):
    """Customer model."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        """To save the data."""

        self.save()

    @staticmethod
    def get_customer_by_email(email: str):
        try:
            return Customer.objects.get(email=email)
        except Customer.DoesNotExist as exc:
            logger.exception(str(exc))
            raise exc

    def exists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
