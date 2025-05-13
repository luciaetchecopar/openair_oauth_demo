import os
from collections import defaultdict
import csv

def summarize_billable_hours(entries):
    user_hours = defaultdict(float)
    for entry in entries:
        user_id = entry.get("userId")
        hours = entry.get("decimalHours", 0)
        user_hours[user_id] += hours
    return dict(user_hours)


def save_summary_to_csv(summary, filename, start_date=None, end_date=None):
    base_path = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(base_path, filename))

    with open(full_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["userId", "total_billable_hours", "start_date", "end_date"])
        for user_id, total_hours in summary.items():
            writer.writerow([user_id, f"{total_hours:.2f}", start_date, end_date])
    print(f"✅ Summary saved to {full_path}")


def save_users_to_csv(users, filename="users_summary.csv"):
    base_path = os.path.dirname(__file__)
    full_path = os.path.abspath(os.path.join(base_path, filename))

    with open(full_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "firstName", "lastName", "email"])

        for user in users:
            writer.writerow([
                user.get("id"),
                user.get("firstName", ""),
                user.get("lastName", ""),
                user.get("email", "")
            ])

    print(f"✅ Users saved to {full_path}")
