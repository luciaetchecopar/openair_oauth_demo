from openair_api import get_time_entries

# 🎯 Customize the dates and user ID here
start_date = "2025-04-01"
end_date = "2025-04-30"
user_id = None  # Or set to a specific ID like 1

from pprint import pprint
results = get_time_entries("2025-04-01", "2025-04-30")
pprint(results)
