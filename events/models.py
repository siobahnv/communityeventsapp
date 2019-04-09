from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a tag name (e.g. Diversity).')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    nominator = models.EmailField(max_length=254, help_text='Enter email address.', null=True)
    event_url = models.URLField(max_length=200)
    
    # location
    # country code & region/region code, determined by location
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    start_date = models.DateField()
    end_date = models.DateField()
    # fiscal year/half/quarter # automate on dates
    # month # automate on dates

    cfp_url = models.URLField(max_length=200)
    conference_contact = models.EmailField(max_length=254, help_text='Enter email address.')
    # internal_contact # should this be here? or be visible?
    # comments/history/actions # this shouldn't be visible?
    votes = models.IntegerField()
    # github issue # automate?
    
    # tags - ManyToManyField 
    tag = models.ManyToManyField(Tag, help_text='Select a tag for this event.')

    class Meta:
        ordering = ['-start_date', 'event_name']

    def __str__(self):
        return self.event_name

class Report(models.Model):
    # foreign key to Event...
    report_title = models.CharField(max_length=100)
    action_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    # sponsored
    # followup_w_nominee
    # execution_date
    # notes/comments/history
    # audience_reach
    # expected_attendance_num
    # attendee_type
    # suggested_elastic_attendees
    # event_brief_url
    # report_url
    # tags

    def __str__(self):
        return self.report_title

class Sponsorship(models.Model):
    # foreign key to Event...?
    action_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )

    # status (proposed/accept/done)
    STATUS_CHOICES = (
        ('p', 'Proposed'),
        ('a', 'Accepted'),
        ('d', 'Done'),
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='p',
    )

    event_rating = models.CharField(max_length=250, help_text='Enter text.', null=True) # not be visible?
    primary_goals = models.TextField(null=True)

    # start_date = models.DateField() # automate from event
    # end_date = models.DateField() # automate from event

    # rec'd sponsorship level
    sponsored_before = models.BooleanField()
    # proposed sponsor amt
    # actual sponsor amt
    # payment currency
    # amt in local currency

    # tags

    def __str__(self):
        return self.status # for now...