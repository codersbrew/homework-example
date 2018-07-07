import json


class BaseObject:

    def initialize(self, raw_value):
        self._raw_value = raw_value

    # Serializer methods for dict based value objects (initialized with {})
    def serialize_with(self, **entry):
        self._raw_value.update(entry)

    def serialize_from_value(self, value):
        self._raw_value.update(value.raw)

    # Serializer methods for array based value objects (initialized with [])
    def serialize_and_append(self, entry):
        self._raw_value.append(entry)

    def serialize_and_append_from_value(self, value):
        self._raw_value.append(value.raw)

    def serialize_and_append_from_values(self, values):
        self._raw_value += map(lambda value: value.raw, values)

    @property
    def raw(self):
        return self._raw_value

    def json(self):
        return json.dumps(self._raw_value)
