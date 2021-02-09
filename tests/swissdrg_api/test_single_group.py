from unittest import TestCase

from open_grouper.swissdrg_api.single_group import single_group
from tests.models.test_patient_case import test_patient_case


class TestSingleGroup(TestCase):
    def test_group(self):
        grouper_result = single_group(patient_case=test_patient_case, version="5.3", locale="de")
        expected_grouper_result = {
            'grouperResult': {'drg': 'G67D', 'mdc': '06', 'pccl': 0, 'gst': 'NORMAL_GROUP', 'explanation': ''},
            'supplements': {'patient_id': '', 'total_value': 0, 'supplements': []},
            'effectiveCostWeight': {'effectiveCostWeight': 6630, 'caseFlag': 'UPPER_OUTLIER'},
            'pdx': {'pdxStatus': 'VALID_PDX', 'ccl': 0, 'streichzahl': 0, 'used': True, 'status': 'VALID_DIAGNOSIS',
                    'code': 'A00.0', 'text': 'Cholera durch Vibrio cholerae O:1, Biovar cholerae'}, 'diagnoses': [
                {'ccl': 0, 'streichzahl': 0, 'used': False, 'status': 'VALID_DIAGNOSIS', 'code': 'G53.1',
                 'text': 'Multiple Hirnnervenlähmungen bei anderenorts klassifizierten infektiösen und parasitären Krankheiten {A00-B99}'}],
            'procedures': [
                {'side': 'R', 'dateValid': True, 'sideValid': True, 'used': 'PROC_NOT_USED', 'valid': 'PROC_VALID',
                 'type': 'SRG', 'conflictingDate': False, 'code': '00.12.00',
                 'text': 'Inhalation von Stickstoffmonoxid, Dauer der Behandlung bis unter 48 Stunden'}],
            'drg': {'code': 'G67D',
                    'text': 'Verschiedene Erkrankungen der Verdauungsorgane oder gastrointestinale Blutung oder Ulkuserkrankung',
                    'partition': 'M', 'cost_weight': 0.456, 'avg_stay_duration': 3.9, 'first_day_discount': 1,
                    'discount_per_day': 0.19, 'first_day_surcharge': 8, 'surcharge_per_day': 0.069,
                    'transfer_discount': 0.078, 'exception_from_reuptake': False},
            'mdc': {'code': '06', 'text': 'Krankheiten und Störungen der Verdauungsorgane'}}

        self.assertDictEqual(grouper_result, expected_grouper_result)
