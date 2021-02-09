from marshmallow import Schema, fields


class PatientCase(Schema):
    admission_mode = fields.String()
    age = fields.Integer()
    diagnoses = fields.List(fields.String())
    los = fields.Integer()
    pdx = fields.String()
    procedures = fields.List(fields.Dict())
    respiration_time = fields.Integer()
    separation_mode = fields.String()
    sex = fields.String()
