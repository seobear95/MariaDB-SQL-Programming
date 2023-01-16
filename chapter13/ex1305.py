import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 추가할 회원정보 입력받기
in_memid = input("회원 ID를 입력하세요: ")

# 단계 4: 회원ID 사용 가능 여부 검증하기
query_string = "SELECT COUNT(*) FROM members WHERE memid = ?"
cur.execute(query_string, (in_memid,))
result = cur.fetchone()
cnt = result[0]
# 단계 5: 회원ID가 있는 경우와 없는 경우 처리하기
if cnt == 1:
    # 단계 5-1: 회원ID가 있는 경우 - 사용 불가능
    print("입력한 아이디가 이미 존재하여 사용할 수 없습니다.")
else:
    # 단계 5-2: 회원ID가 없는 경우 - 사용 가능
    # 나머지 회원정보를 추가 입력받기
    in_memname = input("회원 이름을 입력하세요: ")
    in_addr = input("주소를 입력하세요: ")
    # 문자열로 실행할 쿼리문 만들기
    query_string = "INSERT INTO `members`"
    query_string += "(`memid`, `memname`, `addr`) VALUES (?, ?, ?)"
    # 쿼리문 실행과 오류 처리
    try:
        cur.execute(query_string, (in_memid, in_memname, in_addr))
    except mdb.Error as e:
        print(f"Error : {e}")
        print("회원 가입 처리 중 오류가 발생했습니다.")
    else:
        print("회원 가입이 완료되었습니다.")
    finally:
        print("실행 마침")
# 단계 6: 회원ID가 있는 경우와 없는 경우 모두 cur과 conn 닫기
cur.close()
conn.close()
