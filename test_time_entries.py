from openair_api import *
from summary import *

# 🎯 Customize the dates and user ID here
start_date = "2025-04-01"
end_date = "2025-04-30"
user_id = None  # Or set to a specific ID like 1

from pprint import pprint



entries = get_time_entries("2025-04-01", "2025-04-30")
summary = summarize_billable_hours(entries)
save_summary_to_csv(summary)
