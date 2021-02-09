from unittest import TestCase

from open_grouper.models.patient_case import PatientCase

test_patient_case = PatientCase() \
    .set_admission_mode("99") \
    .set_age(23) \
    .add_diagnose("G53.1") \
    .set_los(10) \
    .set_pdx("A00.0") \
    .add_procedure({"code": "00.12.00", "side": "R"}) \
    .set_respiration_time(0) \
    .set_separation_mode("01") \
    .set_sex("M")


class TestPatientCase(TestCase):
    def test_serialization(self):
        serialized_patient_case = test_patient_case.to_dict()
        expected_serialized_case = {"admission_mode": "99", "diagnoses": ["G53.1"], "age": 23, "los": 10,
                                    "pdx": "A00.0", "procedures": [{"code": "00.12.00", "side": "R"}],
                                    "separation_mode": "01", "respiration_time": 0, "sex": "M"}

        self.assertDictEqual(serialized_patient_case, expected_serialized_case)
