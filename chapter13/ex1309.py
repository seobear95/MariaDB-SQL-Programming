# 단계 1: MariaDB 연결 개체 conn 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: database 생성 쿼리문 실행
try:
    query_string = "CREATE DATABASE IF NOT EXISTS `pythontest`"
    cur.execute(query_string)
except:
    print("쿼리문에 문제가 있어 실행하지 못함.")
else:
    print("`pytnontest` DB 생성이 완료되었습니다.")
finally:
    print("실행 마침")
    cur.close()
    conn.close()
