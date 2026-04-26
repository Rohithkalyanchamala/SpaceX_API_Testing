import pytest
base_url="https://api.spacexdata.com/v5" 

@pytest.fixture
def base_url():
    return base_url