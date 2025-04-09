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
        return []

    headers = {
        "Authorization": f"Bearer {token}",
        "X-OpenAir-API-Key": api_key,
        "X-OpenAir-Namespace": namespace,
        "Content-Type": "application/json"
    }
    url = f"{base_url}/users"
    response = requests.get(url, headers=headers)

    try:
        return response.json() if response.ok else {"error": response.text}
    except Exception as e:
        return {"error": str(e)}

def get_time_entries(start_date, end_date, user_id=None, limit=1000):
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

    all_entries = []
    offset = 0
    while True:
        filters = [
            f'accountingDate ON_OR_AFTER "{start_date}"',
            f'accountingDate ON_OR_BEFORE "{end_date}"'
        ]
        if user_id:
            filters.append(f'userId EQUAL {user_id}')

        q = " AND ".join(filters)
        params = {
            "q": q,
            "limit": limit,
            "offset": offset
        }

        print(f"🔍 Fetching time entries... offset={offset}")
        response = requests.get(f"{base_url}/time-entries", headers=headers, params=params)

        if not response.ok:
            print("❌ Failed to fetch time entries:")
            print("Status:", response.status_code)
            print("Response:", response.text)
            return []

        data = response.json().get("data", [])
        all_entries.extend(data)

        meta = response.json().get("meta", {})
        total_rows = meta.get("totalRows", 0)
        offset += limit
        if offset >= total_rows:
            break

    return all_entries
