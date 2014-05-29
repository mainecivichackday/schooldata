from datetime import datetime
from django.db import models
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TitleSlugDescriptionModel, \
    TimeStampedModel

#from .managers import PublicManager


class District(TitleSlugDescriptionModel, TimeStampedModel):
    """
    District model class.
    """

    code = models.CharField(max_length=6)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('district-detail', (), {'slug': self.slug})


class School(TitleSlugDescriptionModel, TimeStampedModel):
    """
    School model class.
    """

    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('school-detail', (), {'slug': self.slug})


class SchoolDataYear(TimeStampedModel):

    school = models.ForeignKey(School)
    year = models.IntegerField(max_length=4)
    enrollment = models.IntegerField(max_length=6)
    free_lunch = models.IntegerField(max_length=6)
    reduced_lunch = models.IntegerField(max_length=6)
    free_reduced_eligible = models.IntegerField(max_lenght=6)
    free_percent = models.FloatField(blank=True, null=True)
    reduced_percent = models.FloatField(blank=True, null=True)
    eligable_percent = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} data for {1}'.format(self.year, self.school)
