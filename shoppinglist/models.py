from django.db import models

class ListItem(models.Model):
    produce = 'VEG'
    chilled = 'CHI'
    household = 'HOU'
    other = 'OTH'
    SECTION_OPTIONS = (
        (produce, 'Produce'),
        (chilled, 'Chilled'),
        (household, 'Household'),
        (other, 'Other'),
    )

    name = models.CharField(max_length=30)
    section = models.CharField(
        max_length = 10,
        choices = SECTION_OPTIONS,
        default = other,
    )
    checked = models.BooleanField()
    displayed = models.BooleanField()

    def __str__(self):
        return self.name
