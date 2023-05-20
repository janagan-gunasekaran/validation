import unittest
from ..validate import get_schema, get_data, validate_json
import os
from ..config import DIRPATH

class TestStringMethods(unittest.TestCase):

    def test_data_json(self):
        data = get_data(f"{DIRPATH}\\src\\data.json")
        schema = get_schema(f"{DIRPATH}\\build_packages\\base.yaml")
        validate = validate_json(data, schema)
        self.assertEqual(validate, True)
