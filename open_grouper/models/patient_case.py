from typing import List, Dict, Optional

from open_grouper.schemas.patient_case import PatientCase as PatienCaseSchema


class PatientCase:
    def __init__(self,
                 admission_mode: Optional[str] = None,
                 age: Optional[int] = None,
                 diagnoses: Optional[List[str]] = None,
                 los: Optional[int] = None,
                 pdx: Optional[str] = None,
                 procedures: Optional[List[Dict]] = None,
                 respiration_time: Optional[int] = None,
                 separation_mode: Optional[str] = None,
                 sex: Optional[str] = None):
        self._admission_mode = admission_mode
        self._age = age
        self._diagnoses = diagnoses or []
        self._los = los
        self._pdx = pdx
        self._procedures = procedures or []
        self._respiration_time = respiration_time
        self._separation_mode = separation_mode
        self._sex = sex

    @property
    def admission_mode(self) -> Optional[str]:
        return self._admission_mode

    @property
    def age(self) -> Optional[int]:
        return self._age

    @property
    def diagnoses(self) -> Optional[List[str]]:
        return self._diagnoses

    @property
    def los(self) -> Optional[int]:
        return self._los

    @property
    def pdx(self) -> Optional[str]:
        return self._pdx

    @property
    def procedures(self) -> Optional[List[Dict]]:
        return self._procedures

    @property
    def respiration_time(self) -> Optional[int]:
        return self._respiration_time

    @property
    def separation_mode(self) -> Optional[str]:
        return self._separation_mode

    @property
    def sex(self) -> Optional[str]:
        return self._sex

    def set_admission_mode(self, admission_mode: str) -> "PatientCase":
        self._admission_mode = admission_mode
        return self

    def set_age(self, age: int) -> "PatientCase":
        self._age = age
        return self

    def set_diagnoses(self, diagnoses: List[str]) -> "PatientCase":
        self._diagnoses = diagnoses
        return self

    def set_los(self, los: int) -> "PatientCase":
        self._los = los
        return self

    def set_pdx(self, pdx: str) -> "PatientCase":
        self._pdx = pdx
        return self

    def set_procedures(self, procedures: List[Dict]) -> "PatientCase":
        self._procedures = procedures
        return self

    def set_respiration_time(self, respiration_time: int) -> "PatientCase":
        self._respiration_time = respiration_time
        return self

    def set_separation_mode(self, separation_mode: str) -> "PatientCase":
        self._separation_mode = separation_mode
        return self

    def set_sex(self, sex: str) -> "PatientCase":
        self._sex = sex
        return self

    def add_diagnose(self, diagnose: str) -> "PatientCase":
        self._diagnoses.append(diagnose)
        return self

    def add_procedure(self, procedure: Dict) -> "PatientCase":
        self._procedures.append(procedure)
        return self

    def to_dict(self) -> Dict:
        schema = PatienCaseSchema()
        return schema.dump(self)
