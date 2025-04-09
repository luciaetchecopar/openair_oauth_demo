import requests
from token_store import load_tokens, is_token_expired
from refresh_token import refresh_access_token

api_key = "SJTZWRmQc3FE726EmgU5"
namespace = "default"
base_url = "https://7050007-blend360-llc.app.sandbox.netsuitesuiteprojectspro.com/rest/v1"

def get_access_token():
    tokens = load_tokens()
    if not tokens or is_token_expired():
        return refresh_access_token()
    return tokens["access_token"]

def inspect_time_entries_metadata():
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

    url = f"{base_url}/time-entries"
    response = requests.options(url, headers=headers)

    print("🔍 OPTIONS /time-entries/ metadata:")
    print("Status Code:", response.status_code)
    print("Response:\n", response.text)

if __name__ == "__main__":
    inspect_time_entries_metadata()
