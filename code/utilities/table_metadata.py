tableList = {
    "STACKEXCHANGE_USER": ["USERID","REPUTATION"],
    "GITHUB_USER": ["USERNAME"],
}

import sqlite3
import os
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir,"hushhush.db")
print(f'db path is {db_path}')
con = sqlite3.connect(db_path,check_same_thread=False)