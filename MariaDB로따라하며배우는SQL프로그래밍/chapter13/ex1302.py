import mariadb as mdb
import sys

# 단계 1: MariaDB 연결 정보를 사용하여 conn 개체 생성
try:
    conn = mdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Kamebook0#!!",
        database="kamebook",
        autocommit=True
    )
except mdb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
