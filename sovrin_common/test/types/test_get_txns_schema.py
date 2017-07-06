import pytest
from sovrin_common.types import ClientGetTxnsOperation
from collections import OrderedDict
from plenum.common.messages.fields import ConstantField


EXPECTED_ORDERED_FIELDS = OrderedDict([
    ("type", ConstantField),
])


def test_has_expected_fields():
    actual_field_names = OrderedDict(ClientGetTxnsOperation.schema).keys()
    assert actual_field_names == EXPECTED_ORDERED_FIELDS.keys()


def test_has_expected_validators():
    schema = dict(ClientGetTxnsOperation.schema)
    for field, validator in EXPECTED_ORDERED_FIELDS.items():
        assert isinstance(schema[field], validator)
