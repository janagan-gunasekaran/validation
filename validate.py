import json
import yaml
from jsonschema import validate
from jsonschema import ValidationError, RefResolutionError

def get_schema(file_name):
    with open(file_name, 'r') as file:
        schema = yaml.safe_load(file)
    return schema

def get_data(file_name):
    with open(file_name, 'r') as file:
        jsonData = json.load(file)
    return jsonData

def validate_json(json_data, schema_data):
    try:
        validate(instance=json_data, schema=schema_data)
    except (ValidationError, RefResolutionError) as err:
        return False

    return True

