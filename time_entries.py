from openair_api.summary import *
from openair_api.openair_execute import *

# 🎯 Customize the dates and user ID here
start_date = "2025-04-01"
end_date = "2025-04-30"
user_id = None  # Or set to a specific ID like 1

entries = get_time_entries(start_date, end_date)
summary = summarize_billable_hours(entries)
save_summary_to_csv(summary, "../billable_hours_summary.csv", start_date=start_date, end_date=end_date)
