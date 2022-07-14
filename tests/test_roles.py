from typing import List, Set

import pytest

from dhos_users_api import roles
from dhos_users_api.roles import UserPermission, UserRole


@pytest.mark.usefixtures("app")
class TestRoles:
    @pytest.mark.parametrize(
        "assigned_roles,expected_permissions",
        [
            [
                [UserRole.GDM_CLINICIAN.value, UserRole.SEND_CLINICIAN.value],
                {
                    UserPermission.READ_GDM_ACTIVATION.value,
                    UserPermission.READ_GDM_ANSWER_ALL.value,
                    UserPermission.READ_GDM_BG_READING_ALL.value,
                    UserPermission.READ_GDM_CLINICIAN.value,
                    UserPermission.READ_GDM_CSV.value,
                    UserPermission.READ_GDM_LOCATION.value,
                    UserPermission.READ_GDM_MEDICATION.value,
                    UserPermission.READ_GDM_MESSAGE.value,
                    UserPermission.READ_GDM_PATIENT.value,
                    UserPermission.READ_GDM_PDF.value,
                    UserPermission.READ_GDM_QUESTION.value,
                    UserPermission.READ_GDM_TELEMETRY_ALL.value,
                    UserPermission.READ_GDM_TRUSTOMER.value,
                    UserPermission.READ_SEND_CLINICIAN.value,
                    UserPermission.READ_SEND_ENCOUNTER.value,
                    UserPermission.READ_SEND_LOCATION.value,
                    UserPermission.READ_SEND_OBSERVATION.value,
                    UserPermission.READ_SEND_PATIENT.value,
                    UserPermission.READ_SEND_PDF.value,
                    UserPermission.READ_SEND_RULE.value,
                    UserPermission.READ_SEND_TRUSTOMER.value,
                    UserPermission.READ_WARD_REPORT.value,
                    UserPermission.WRITE_GDM_ACTIVATION.value,
                    UserPermission.WRITE_GDM_ALERT.value,
                    UserPermission.WRITE_GDM_ANSWER_ALL.value,
                    UserPermission.WRITE_GDM_CLINICIAN.value,
                    UserPermission.WRITE_GDM_MESSAGE.value,
                    UserPermission.WRITE_GDM_PATIENT.value,
                    UserPermission.WRITE_GDM_PDF.value,
                    UserPermission.WRITE_GDM_SMS.value,
                    UserPermission.WRITE_GDM_SURVEY.value,
                    UserPermission.WRITE_GDM_TELEMETRY.value,
                    UserPermission.WRITE_GDM_TERMS_AGREEMENT.value,
                    UserPermission.WRITE_SEND_ENCOUNTER.value,
                    UserPermission.WRITE_SEND_OBSERVATION.value,
                    UserPermission.WRITE_SEND_PATIENT.value,
                    UserPermission.WRITE_SEND_TERMS_AGREEMENT.value,
                },
            ],
            [
                [
                    UserRole.GDM_CLINICIAN.value,
                    UserRole.GDM_SUPERCLINICIAN.value,
                    UserRole.GDM_ADMINISTRATOR.value,
                ],
                {
                    UserPermission.DELETE_GDM_ARTICLE.value,
                    UserPermission.DELETE_GDM_MEDICATION.value,
                    UserPermission.READ_GDM_ACTIVATION.value,
                    UserPermission.READ_GDM_ANSWER_ALL.value,
                    UserPermission.READ_GDM_BG_READING_ALL.value,
                    UserPermission.READ_GDM_CLINICIAN_ALL.value,
                    UserPermission.READ_GDM_CLINICIAN.value,
                    UserPermission.READ_GDM_CSV.value,
                    UserPermission.READ_GDM_LOCATION_ALL.value,
                    UserPermission.READ_GDM_LOCATION.value,
                    UserPermission.READ_GDM_MEDICATION.value,
                    UserPermission.READ_GDM_MESSAGE_ALL.value,
                    UserPermission.READ_GDM_MESSAGE.value,
                    UserPermission.READ_GDM_PATIENT_ALL.value,
                    UserPermission.READ_GDM_PATIENT.value,
                    UserPermission.READ_GDM_PDF.value,
                    UserPermission.READ_GDM_QUESTION.value,
                    UserPermission.READ_GDM_TELEMETRY_ALL.value,
                    UserPermission.READ_GDM_TRUSTOMER.value,
                    UserPermission.WRITE_GDM_ACTIVATION.value,
                    UserPermission.WRITE_GDM_ALERT.value,
                    UserPermission.WRITE_GDM_ANSWER_ALL.value,
                    UserPermission.WRITE_GDM_ARTICLE.value,
                    UserPermission.WRITE_GDM_CLINICIAN_ALL.value,
                    UserPermission.WRITE_GDM_CLINICIAN.value,
                    UserPermission.WRITE_GDM_LOCATION.value,
                    UserPermission.WRITE_GDM_MEDICATION.value,
                    UserPermission.WRITE_GDM_MESSAGE_ALL.value,
                    UserPermission.WRITE_GDM_MESSAGE.value,
                    UserPermission.WRITE_GDM_PATIENT_ALL.value,
                    UserPermission.WRITE_GDM_PATIENT.value,
                    UserPermission.WRITE_GDM_PDF.value,
                    UserPermission.WRITE_GDM_QUESTION.value,
                    UserPermission.WRITE_GDM_SMS.value,
                    UserPermission.WRITE_GDM_SURVEY.value,
                    UserPermission.WRITE_GDM_TELEMETRY.value,
                    UserPermission.WRITE_GDM_TERMS_AGREEMENT.value,
                },
            ],
            [
                [UserRole.SYSTEM.value],
                {
                    UserPermission.DELETE_GDM_ARTICLE.value,
                    UserPermission.DELETE_GDM_MEDICATION.value,
                    UserPermission.DELETE_GDM_SMS.value,
                    UserPermission.READ_AUDIT_EVENT.value,
                    UserPermission.READ_DBM_CLINICIAN_ALL.value,
                    UserPermission.READ_ERROR_MESSAGE.value,
                    UserPermission.READ_FAILED_REQUEST_QUEUE.value,
                    UserPermission.READ_GDM_ACTIVATION.value,
                    UserPermission.READ_GDM_ANSWER_ALL.value,
                    UserPermission.READ_GDM_BG_READING_ALL.value,
                    UserPermission.READ_GDM_CLINICIAN_ALL.value,
                    UserPermission.READ_GDM_LOCATION_ALL.value,
                    UserPermission.READ_GDM_MEDICATION.value,
                    UserPermission.READ_GDM_MESSAGE_ALL.value,
                    UserPermission.READ_GDM_PATIENT_ALL.value,
                    UserPermission.READ_GDM_PDF.value,
                    UserPermission.READ_GDM_QUESTION.value,
                    UserPermission.READ_GDM_RULE.value,
                    UserPermission.READ_GDM_SMS.value,
                    UserPermission.READ_GDM_SURVEY_ALL.value,
                    UserPermission.READ_GDM_TELEMETRY_ALL.value,
                    UserPermission.READ_GDM_TELEMETRY.value,
                    UserPermission.READ_GDM_TRUSTOMER.value,
                    UserPermission.READ_HL7_MESSAGE.value,
                    UserPermission.READ_LOCATION_ALL.value,
                    UserPermission.READ_LOCATION_BY_ODS.value,
                    UserPermission.READ_SEND_CLINICIAN_ALL.value,
                    UserPermission.READ_SEND_CLINICIAN.value,
                    UserPermission.READ_SEND_DEVICE.value,
                    UserPermission.READ_SEND_ENCOUNTER.value,
                    UserPermission.READ_SEND_ENTRY_IDENTIFIER.value,
                    UserPermission.READ_SEND_LOCATION.value,
                    UserPermission.READ_SEND_OBSERVATION.value,
                    UserPermission.READ_SEND_PATIENT.value,
                    UserPermission.READ_SEND_PDF.value,
                    UserPermission.READ_SEND_RULE.value,
                    UserPermission.READ_SEND_TRUSTOMER.value,
                    UserPermission.READ_WARD_REPORT.value,
                    UserPermission.WRITE_AUDIT_EVENT.value,
                    UserPermission.WRITE_ERROR_MESSAGE.value,
                    UserPermission.WRITE_FAILED_REQUEST_QUEUE.value,
                    UserPermission.WRITE_GDM_ACTIVATION.value,
                    UserPermission.WRITE_GDM_ALERT.value,
                    UserPermission.WRITE_GDM_ARTICLE.value,
                    UserPermission.WRITE_GDM_BG_READING.value,
                    UserPermission.WRITE_GDM_CLINICIAN_ALL.value,
                    UserPermission.WRITE_GDM_CSV.value,
                    UserPermission.WRITE_GDM_LOCATION.value,
                    UserPermission.WRITE_GDM_MEDICATION.value,
                    UserPermission.WRITE_GDM_MESSAGE_ALL.value,
                    UserPermission.WRITE_GDM_PATIENT_ALL.value,
                    UserPermission.WRITE_GDM_PDF.value,
                    UserPermission.WRITE_GDM_QUESTION.value,
                    UserPermission.WRITE_GDM_SMS.value,
                    UserPermission.WRITE_GDM_SURVEY.value,
                    UserPermission.WRITE_GDM_TELEMETRY.value,
                    UserPermission.WRITE_GDM_TERMS_AGREEMENT.value,
                    UserPermission.WRITE_HL7_MESSAGE.value,
                    UserPermission.WRITE_LOCATION.value,
                    UserPermission.WRITE_PATIENT_CSV.value,
                    UserPermission.WRITE_SEND_CLINICIAN_ALL.value,
                    UserPermission.WRITE_SEND_CLINICIAN.value,
                    UserPermission.WRITE_SEND_DEVICE.value,
                    UserPermission.WRITE_SEND_ENCOUNTER.value,
                    UserPermission.WRITE_SEND_LOCATION.value,
                    UserPermission.WRITE_SEND_OBSERVATION.value,
                    UserPermission.WRITE_SEND_PATIENT.value,
                    UserPermission.WRITE_SEND_PDF.value,
                    UserPermission.WRITE_WARD_REPORT.value,
                },
            ],
        ],
    )
    def test_get_permissions_for_roles(
        self, assigned_roles: List[str], expected_permissions: Set[str]
    ) -> None:
        actual_permissions = roles.get_permissions_for_roles(assigned_roles)
        assert set(actual_permissions) == expected_permissions

    def test_get_role_map(self) -> None:
        role_map = roles.get_role_map()
        assert set(role_map["System"]) == {
            "delete:gdm_article",
            "delete:gdm_medication",
            "delete:gdm_sms",
            "read:audit_event",
            "read:dbm_clinician_all",
            "read:error_message",
            "read:failed_request_queue",
            "read:gdm_activation",
            "read:gdm_answer_all",
            "read:gdm_bg_reading_all",
            "read:gdm_clinician_all",
            "read:gdm_location_all",
            "read:gdm_medication",
            "read:gdm_message_all",
            "read:gdm_patient_all",
            "read:gdm_pdf",
            "read:gdm_question",
            "read:gdm_rule",
            "read:gdm_sms",
            "read:gdm_survey_all",
            "read:gdm_telemetry_all",
            "read:gdm_telemetry",
            "read:gdm_trustomer",
            "read:hl7_message",
            "read:location_all",
            "read:location_by_ods",
            "read:send_clinician_all",
            "read:send_clinician",
            "read:send_device",
            "read:send_encounter",
            "read:send_entry_identifier",
            "read:send_location",
            "read:send_observation",
            "read:send_patient",
            "read:send_pdf",
            "read:send_rule",
            "read:send_trustomer",
            "read:ward_report",
            "write:audit_event",
            "write:error_message",
            "write:failed_request_queue",
            "write:gdm_activation",
            "write:gdm_alert",
            "write:gdm_article",
            "write:gdm_bg_reading",
            "write:gdm_clinician_all",
            "write:gdm_csv",
            "write:gdm_location",
            "write:gdm_medication",
            "write:gdm_message_all",
            "write:gdm_patient_all",
            "write:gdm_pdf",
            "write:gdm_question",
            "write:gdm_sms",
            "write:gdm_survey",
            "write:gdm_telemetry",
            "write:gdm_terms_agreement",
            "write:hl7_message",
            "write:location",
            "write:patient_csv",
            "write:send_clinician_all",
            "write:send_clinician",
            "write:send_device",
            "write:send_encounter",
            "write:send_location",
            "write:send_observation",
            "write:send_patient",
            "write:send_pdf",
            "write:ward_report",
        }
