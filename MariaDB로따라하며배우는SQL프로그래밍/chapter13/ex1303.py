import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 문자열로 실행할 쿼리문 만들기
query_string1 = "SELECT memid, memname, addr FROM `members` "
query_string2 = "SELECT memid, memname, addr FROM `members` "
query_string2 += " WHERE memname LIKE ?"

# 단계 4: 쿼리문에서 사용할 데이터 만들기
query_params = [('%홍%')]

# 단계 5: 쿼리문 실행과 조회한 결과 출력하기
try:
    cur.execute(query_string1)
    dataLists = cur.fetchall()
    for memid, memname, addr in dataLists:
        print(memid, memname, addr)
    print('---------------------------------')
    cur.execute(query_string2, query_params)
    dataLists = cur.fetchall()
    for memid, memname, addr in dataLists:
        print(memid, memname, addr)
    print('---------------------------------')
except mdb.Error as e:
    print("쿼리문에 문제가 있어 실행하지 못함..")
    print(e)
finally:
    print("실행 마침")
    cur.close()
    conn.close()
