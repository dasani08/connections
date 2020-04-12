from marshmallow import fields
from marshmallow_enum import EnumField

from connections.extensions import ma
from connections.models.connection import Connection, ConnectionType
from connections.models.person import Person


class BaseModelSchema(ma.ModelSchema):
    def __init__(self, strict=True, **kwargs):
        super().__init__(strict=strict, **kwargs)


class PersonSchema(BaseModelSchema):

    email = fields.Email()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email')


class ConnectionSchema(BaseModelSchema):
    from_person_id = fields.Integer()
    to_person_id = fields.Integer()
    connection_type = EnumField(ConnectionType)
    from_person = fields.Nested(PersonSchema)
    to_person = fields.Nested(PersonSchema)

    class Meta:
        model = Connection
