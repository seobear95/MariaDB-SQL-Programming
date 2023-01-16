import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 데이터를 변경할 ‘회원 ID’ 입력받기
in_memid = input("삭제할 회원 ID를 입력하세요: ")

# 단계 4: 입력한 ‘회원 ID’로 변경전 회원 이름과 주소를 조회한다.
query_str = "SELECT memname, addr FROM members where memid = ? "
cur.execute(query_str, (in_memid,))
result = cur.fetchone()

# 단계 5: 입력한 ‘회원ID’가 있는 경우와 없는 경우 처리
if result is not None:  # 검색한 결과가 있는 경우
    name = result[0]   # 검색한 결과의 첫 번째 열, memname
    addr = result[1]   # 검색한 결과의 두 번째 열, addr
    # 삭제전의 데이터를 화면에 출력
    print("--< 삭제할 회원정보 >--------------------------")
    print("회원 ID : ", in_memid)
    print("회원이름 : ", name)
    print("회원주소 : ", addr)
    print("------------------------------------")

    # 단계 6: 삭제 여부 확인하기
    enable = input("삭제 여부 Y 또는 N 입력: ")
    if enable.lower() == 'y':    # 삭제 여부에서 ‘Y’인경우
        try:
            # 단계 7: DELETE 쿼리문으로 데이터 삭제
            query_string = "DELETE FROM `members` WHERE memid = ?"
            cur.execute(query_string, (in_memid,))
            print("회원정보가 삭제되었습니다.")
        except:
            print("쿼리문에 문제가 있어 실행이 되지 않았습니다.")
    else:   # 삭제 여부에서 ‘Y’가 아닌 경우
        print("회원정보를 삭제하지 않았습니다.")
else:
    print("삭제할 회원정보가 존재하지 않습니다.")

# 단계 8: 프로그램 종료하기
cur.close()
conn.close()
