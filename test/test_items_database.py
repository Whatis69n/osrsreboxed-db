"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Tests for module: docs/items-json

Copyright (c) 2020, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
import json
from pathlib import Path

import config
import validator


def test_item_database():
    """Unit test to check item database contents against JSON schema."""
    # Read in the item schema file
    path_to_schema = Path(config.DATA_SCHEMAS_PATH / "schema-items.json")
    with open(path_to_schema, 'r') as f:
        schema = json.loads(f.read())

    # Validator object with schema attached
    v = validator.MyValidator(schema)

    # Set the path to the items-json folder and get all the JSON files
    path_to_items_json_dir = Path(config.DOCS_PATH / "items-json")
    fis = path_to_items_json_dir.glob("*.json")
    fis = sorted(fis)

    # Validate each file
    for json_file in fis:
        with open(json_file) as fi:
            item = json.load(fi)
            # Validate the item and capture the result
            is_valid = v.validate(item)
            if not is_valid:
                # Print the item and the validation error
                print(f"Validation failed for item: {json_file}")
                print(f"Item content: {json.dumps(item, indent=2)}")
                print(f"Validation errors: {v.errors}")
            assert is_valid, f"Validation failed for item: {json_file}"
