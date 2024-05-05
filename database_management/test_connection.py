import sys

import pypyodbc

DRIVER = "SQL Server"
SERVER_NAME = "BRYCEPC\MSSQLSERVER01"
DATABASE_NAME = "IronAndBlood"

connection = f"""Driver={{{DRIVER}}};
                    Server={SERVER_NAME};
                    Database={DATABASE_NAME};
                    Trust_Connection=yes;
    """
try:
    conn = pypyodbc.connect(connection)
    print('connection is successful')
except Exception as e:
    print(e)
    print("task is terminated")
    sys.exit()
else:
    cursor = conn.cursor()