import os
from django.conf import settings

from django.apps import AppConfig
from edc_protocol.apps import AppConfig as EdcProtocolAppConfigParent
from edc_appointment.apps import AppConfig as EdcAppointmentAppConfigParent
from django_crypto_fields.apps import DjangoCryptoFieldsAppConfig as DjangoCryptoFieldsAppConfigParent
from edc_label.apps import AppConfig as EdcLabelAppConfigParent
from edc_registration.apps import AppConfig as EdcRegistrationAppConfigParent

from edc_consent.apps import AppConfig as EdcConsentAppConfigParent
from edc_timepoint.apps import AppConfig as EdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_consent.consent_config import ConsentConfig
from edc_metadata.apps import AppConfig as EdcMetaDataAppConfigParent
from datetime import datetime


class AmpAppConfig(AppConfig):
    name = 'amp'
    protocol_number = 'HVTN 081'
    datafax_site_number = 283
    datafax_site_name = 'Botswana, Gabarone'
    institution = 'Botswana Harvard AIDS Institute Partnership'
    verbose_name = 'AMP Study'
    device_id = 91


class EdcConsentAppConfig(EdcConsentAppConfigParent):
    consent_configs = [
        ConsentConfig(
            'amp.screeningconsent',
            version='1',
            start=datetime(2016, 5, 1, 0, 0, 0).replace(tzinfo=None),
            end=datetime(2016, 10, 20, 0, 0, 0).replace(tzinfo=None),
            age_min=16,
            age_is_adult=18,
            age_max=64,
            gender=['M', 'F']
        )
    ]
#         ConsentConfig(
#             'amp.studyconsent',
#             version='2',
#             start=datetime(2016, 9, 30, 0, 0, 0).replace(tzinfo=None),
#             end=datetime(2017, 5, 1, 0, 0, 0).replace(tzinfo=None),
#             age_min=16,
#             age_is_adult=18,
#             age_max=64,
#             gender=['M', 'F']
#         ),


class DjangoCryptoFieldsAppConfig(DjangoCryptoFieldsAppConfigParent):
    name = 'django_crypto_fields'
    model = ('django_crypto_fields', 'crypt')


class EdcTimepointAppConfig(EdcTimepointAppConfig):
    timepoints = [
        Timepoint(
            model='amp.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='CLOSED'
        )
    ]


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = None
    default_printer_label = 'AmpZplPrinter'
    print ("settings.STATIC_ROOT", settings.STATIC_ROOT)
    default_template_folder = os.path.join(settings.STATIC_ROOT, 'templates', 'label_templates')
    extra_templates_folder = os.path.join(settings.STATIC_ROOT, 'amp', 'label_templates')


class EdcRegistrationAppConfig(EdcRegistrationAppConfigParent):
    app_label = 'amp'


class EdcProtocolAppConfig(EdcProtocolAppConfigParent):
    enrollment_caps = {'amp.enrollment': ('subject', 500)}  # {label_lower: (key, count)}


class EdcAppointmentAppConfig(EdcAppointmentAppConfigParent):
    app_label = 'amp'


class EdcMetaDataAppConfig(EdcMetaDataAppConfigParent):
    model_attrs = [('amp', 'crfmetadata'), ('amp', 'requisitionmetadata')]
    reason_field = {'amp.subjectvisit': 'reason'}
    app_label = 'amp'
