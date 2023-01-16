import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 추가할 회원정보 입력받기
in_memid = input("회원 ID를 입력하세요: ")
in_memname = input("회원 이름을 입력하세요: ")
in_addr = input("주소를 입력하세요: ")

# 단계 4: 문자열로 실행할 쿼리문 만들기
query_string = "INSERT INTO `members`"
query_string += "(`memid`, `memname`, `addr`) VALUES (?, ?, ?)"

# 단계 5: 쿼리문 실행
try:
    cur.execute(query_string, (in_memid, in_memname, in_addr))
except:
    print("쿼리문에 문제가 있어 실행하지 못함.")
finally:
    print("실행 마침")
    cur.close()
    conn.close()
