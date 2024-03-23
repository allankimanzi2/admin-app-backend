import requests

token = ""


def test_validate_endpoint():
    headers = {
        'authorization':token
    }
    response = requests.post(
        "http://127.0.0.1:/ping"
        headers=headers
    )

    return response.text

print(test_validate_endpoint())
