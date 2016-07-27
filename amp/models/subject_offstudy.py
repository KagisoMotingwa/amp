from django.db import models

# from edc_base.audit_trail import AuditTrail
from edc_base.model.models import BaseUuidModel
from edc_consent.models import RequiresConsentMixin
from edc_export.models import ExportTrackingFieldsMixin
from edc_meta_data.managers import CrfMetaDataManager
from edc_offstudy.models import OffStudyModelMixin
# from edc_sync.models import SyncModelMixin

from edc_visit_tracking.models import CrfModelMixin
from .screening_consent import ScreeningConsent
from .subject_visit import SubjectVisit


class SubjectOffStudy(OffStudyModelMixin, CrfModelMixin,
                      RequiresConsentMixin, ExportTrackingFieldsMixin, BaseUuidModel):

    """ A model completed by the user on the visit when the subject is taken off-study. """

    consent_model = ScreeningConsent

    maternal_visit = models.OneToOneField(SubjectVisit)

    entry_meta_data_manager = CrfMetaDataManager(SubjectVisit)

    class Meta:
        app_label = 'amp'
        verbose_name = "Subject Off Study"