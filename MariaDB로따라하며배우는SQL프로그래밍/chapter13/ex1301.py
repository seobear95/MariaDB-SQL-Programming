import mariadb as mdb

# 단계 1: MariaDB 연결 정보
conn_params = {"host": "localhost",
               "port": 3306,
               "user": "root",
               "password": "Kamebook0#!!"}

# 단계 2: 연결 정보를 사용하여 MariaDB Connection 개체 생성하기
conn = mdb.connect(**conn_params)

# 단계 3: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 4: 쿼리문 실행
cur.execute("SHOW databases")

# 단계 5: 커서 개체로부터 결과 가져오기
databaseList = cur.fetchall()

# 단계 6: 반복문으로 결과 출력하기
for database in databaseList:
    print(database)

# 단계 7: 커넥션 종료하기
cur.close()
conn.close()
