from openair_api import *
from summary import *

users = get_users()
save_users_to_csv(users, "users_summary.csv")
