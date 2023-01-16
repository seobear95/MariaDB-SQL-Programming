import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 추가할 회원정보 입력받기
in_memid = input("회원 ID를 입력하세요: ")
in_memname = input("회원 이름을 입력하세요: ")
in_birth = input("생년월일을 입력하세요: ")
args = (in_memid, in_memname, in_birth, 0)

# 단계 4: 저장 프로시저를 호출하면서 입력받은 회원정보를 전달한다.
cur.callproc('sp_members_insert', args)

result = cur.fetchone()
rv = result[0]
if rv == 1:
    print("회원 가입이 완료되었습니다.")
else:
    print("회원 가입에 실패했습니다.")

# 단계 5: 프로그램 종료하기
cur.close()
conn.close()
