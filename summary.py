from collections import defaultdict
import csv

def summarize_billable_hours(entries):
    user_hours = defaultdict(float)

    for entry in entries:
        user_id = entry.get("userId")
        hours = entry.get("decimalHours", 0)
        user_hours[user_id] += hours

    return dict(user_hours)


def save_summary_to_csv(summary, filename="billable_hours_summary.csv"):
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["userId", "total_billable_hours"])
        for user_id, total_hours in summary.items():
            writer.writerow([user_id, f"{total_hours:.2f}"])
    print(f"✅ Summary saved to {filename}")
