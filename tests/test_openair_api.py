from unittest.mock import patch, Mock
from openair_api.openair_execute import get_users

@patch("openair_api.openair_execute.get_access_token", return_value="fake_token")
@patch("openair_api.openair_execute.requests.get")
def test_get_users(mock_get, mock_token):
    # Simula dos llamadas paginadas a /users
    mock_get.side_effect = [
        Mock(ok=True, json=lambda: {
            "data": [{"id": 1, "firstName": "Alice"}],
            "meta": {"totalRows": 2}
        }),
        Mock(ok=True, json=lambda: {
            "data": [{"id": 2, "firstName": "Bob"}],
            "meta": {"totalRows": 2}
        })
    ]

    users = get_users(limit=1)
    assert len(users) == 2
    assert users[0]["id"] == 1
    assert users[1]["id"] == 2
