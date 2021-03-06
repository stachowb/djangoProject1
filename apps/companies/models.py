from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy


class Company(models.Model):
    """
    Abstract representation of a company that a driver works for
    """
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.__str__())
        super(Company, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('company-view', kwargs={"slug": self.slug})
