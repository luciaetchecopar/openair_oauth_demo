from openair_api import get_users

print("\n🔍 Fetching users from OpenAir...")
data = get_users()
print("\nResponse:")
print(data)