from openair_api.summary import *
from openair_api.openair_execute import *


users = get_users()
save_users_to_csv(users, "../users_summary.csv")
