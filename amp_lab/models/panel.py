from django.db import models

from .aliquot_type import AliquotType
from edc_base.model.models.base_uuid_model import BaseUuidModel


class Panel(BaseUuidModel):

    name = models.CharField(max_length=25)

    aliquot_type = models.ManyToManyField(
        AliquotType,
        help_text='Choose all that apply',)

    #panel_type = models.CharField(max_length=15, choices=PANEL_TYPE, default='TEST')

    def natural_key(self):
        return (self.name, )

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'amp_lab'
