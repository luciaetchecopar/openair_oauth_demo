import requests
from token_store import load_tokens, is_token_expired
from refresh_token import refresh_access_token

api_key = "SJTZWRmQc3FE726EmgU5"
namespace = "default"
base_url = "https://7050007-blend360-llc.app.sandbox.netsuitesuiteprojectspro.com/rest/v1"

def get_access_token():
    tokens = load_tokens()
    if not tokens:
        return refresh_access_token()
    if is_token_expired():
        return refresh_access_token()
    return tokens["access_token"]

def get_users():
    token = get_access_token()
    if not token:
        print("❌ No valid token available.")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "X-OpenAir-API-Key": api_key,
        "X-OpenAir-Namespace": namespace,
        "Content-Type": "application/json"
    }
    url = f"{base_url}/users"
    response = requests.get(url, headers=headers)
    return response.json() if response.ok else response.text