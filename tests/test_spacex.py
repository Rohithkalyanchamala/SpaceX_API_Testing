import requests

BASE_URL = "https://api.spacexdata.com/v4"

# TEST 1 - Get all launches
def test_get_all_launches():
    response = requests.get(f"{BASE_URL}/launches")
    assert response.status_code == 200

# TEST 2 - Launches list is not empty
def test_launches_not_empty():
    response = requests.get(f"{BASE_URL}/launches")
    data = response.json()
    assert len(data) > 0

# TEST 3 - Get all rockets
def test_get_all_rockets():
    response = requests.get(f"{BASE_URL}/rockets")
    assert response.status_code == 200

# TEST 4 - Rockets list is not empty
def test_rockets_not_empty():
    response = requests.get(f"{BASE_URL}/rockets")
    data = response.json()
    assert len(data) > 0

# TEST 5 - Get all crew members
def test_get_all_crew():
    response = requests.get(f"{BASE_URL}/crew")
    assert response.status_code == 200

# TEST 6 - Get all launchpads
def test_get_all_launchpads():
    response = requests.get(f"{BASE_URL}/launchpads")
    assert response.status_code == 200

# TEST 7 - Get all capsules
def test_get_all_capsules():
    response = requests.get(f"{BASE_URL}/capsules")
    assert response.status_code == 200

# TEST 8 - Get invalid endpoint
def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalidendpoint")
    assert response.status_code == 404

# TEST 9 - Get all payloads
def test_get_all_payloads():
    response = requests.get(f"{BASE_URL}/payloads")
    assert response.status_code == 200