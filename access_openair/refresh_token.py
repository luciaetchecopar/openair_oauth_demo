import base64
import requests
import time
from access_openair.token_store import save_tokens, load_tokens

client_id = "78517_1vJn9AI90xztYVfn"
client_secret = "Ay1YHnzy-2-CkfVAudfdDgECt3fa1IeA2BhPopnOdCTgpkjCEcFyiLGT3wjOLSb7EylFkLsFIbWxddXAEBhCwA"
redirect_uri = "http://localhost:3000/callback"
sandbox_domain = "7050007-blend360-llc.app.sandbox.netsuitesuiteprojectspro.com"

def refresh_access_token():
    tokens = load_tokens()
    if not tokens:
        print("No existing tokens found.")
        return None

    refresh_token = tokens["refresh_token"]

    token_url = f"https://{sandbox_domain}/login/oauth2/v1/token"
    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "redirect_uri": redirect_uri
    }

    print("Refreshing access token...")
    response = requests.post(token_url, headers=headers, data=data)

    if response.ok:
        new_tokens = response.json()
        expires_at = int(time.time()) + new_tokens["expires_in"]
        save_tokens(new_tokens["access_token"], new_tokens["refresh_token"], new_tokens["expires_in"], expires_at)
        print("✅ Access token refreshed!")
        return new_tokens["access_token"]
    else:
        print("❌ Failed to refresh token:", response.text)
        return None
