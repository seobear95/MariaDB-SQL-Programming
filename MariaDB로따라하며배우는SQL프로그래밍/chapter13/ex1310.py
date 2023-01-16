import mariadb as mdb
from ex1302 import conn

conn.database = 'pythontest'
conn.autocommit = False

cur = conn.cursor()

query_string = "CREATE TABLE python_members( "
query_string += "  seq INT(11) NOT NULL AUTO_INCREMENT, "
query_string += "  id VARCHAR(5) NOT NULL "
query_string += "      COLLATE 'utf8mb4_general_ci', "
query_string += "  name VARCHAR(50) NULL DEFAULT NULL "
query_string += "      COLLATE 'utf8mb4_general_ci', "
query_string += "  email VARCHAR(100) NULL DEFAULT NULL "
query_string += "      COLLATE 'utf8mb4_general_ci', "
query_string += "  PRIMARY KEY (seq, id) USING BTREE "
query_string += "  ) "
query_string += "  COLLATE = 'utf8mb4_general_ci' "
query_string += "  ENGINE=INNODB"
try:
    cur.execute(query_string)
    conn.commit()

    cur.execute("SHOW TABLES")
    tableList = cur.fetchall()
    for table in tableList:
        print(table)
except mdb.Error as e:
    print(f"Error : ", e)
    print("쿼리문에 문제가 있어 실행하지 못함.")

else:
    print("테이블 생성이 완료되었습니다.")

finally:
    print("실행마침")
    cur.close()
    conn.close()
