from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy
from apps.companies.models import Company


class Driver(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    VEHICLE_CHOICES = (
        (1, "Trekker"),
        (2, "Containerbil m/løftelem"),
        (3, "Containerbil"),
        (4, "-")
    )

    vehicle = models.IntegerField(choices=VEHICLE_CHOICES)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.id) + self.__str__())
        super(Driver, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('driver-view', kwargs={"slug": self.slug})
