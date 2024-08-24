import os
import json

import pytest

@pytest.fixture(autouse=False)
def load_test_data(request):
    file_name = request.param
    directory_path = 'testdata'
    file_path = os.path.join(directory_path, file_name)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        raise FileNotFoundError(f"TestData is not exist.")

