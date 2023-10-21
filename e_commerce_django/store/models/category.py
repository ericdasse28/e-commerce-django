from django.db import models


class Category(models.Model):
    """Category model."""

    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        """Get all product categories."""
        return Category.objects.all()

    def __str__(self) -> str:
        return self.name
