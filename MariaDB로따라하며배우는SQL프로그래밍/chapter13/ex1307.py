import mariadb as mdb

# 단계 1: MariaDB 연결개체 가져오기
from ex1302 import conn

# 단계 2: 쿼리문의 실행 결과를 담을 커서 개체 생성
cur = conn.cursor()

# 단계 3: 데이터를 변경할 ‘회원 ID' 입력받기
in_memid = input("변경할 회원 ID를 입력하세요: ")

# 단계 4: 입력한 ‘회원 ID'로 변경전 회원 이름과 주소를 조회한다.
query_str = "SELECT memname, addr FROM members where memid = ? "
cur.execute(query_str, (in_memid,))
result = cur.fetchone()

# 단계 5: 입력한 ‘회원ID'가 있는 경우와 없는 경우 처리
if result is not None:  # 검색한 결과가 있는 경우
    name = result[0]   # 검색한 결과의 첫 번째 열, memname
    addr = result[1]   # 검색한 결과의 두 번째 열, addr
    # 변경전의 데이터를 화면에 출력
    print("--< 변경전 >--------------------------")
    print("회원 ID : ", in_memid)
    print("회원이름 : ", name)
    print("회원주소 : ", addr)
    print("------------------------------------")

    # 단계 6: 입력한 ‘회원 ID'로 변경할 ‘회원이름'과 ‘회원주소'를 입력받는다.
    in_memname = input("변경할 회원 이름을 입력하세요: ")
    in_addr = input("변경할 회원 주소를 입력하세요: ")

    try:
        # 단계 7: UPDATE 쿼리문으로 데이터 업데이트
        query_string = "UPDATE members "
        query_string += "SET memname = ?, addr= ? WHERE memid= ? "
        cur.execute(query_string, (in_memname, in_addr, in_memid))
    except mdb.Error as e:
        print(f"Error : {e}")
        print("회원정보 변경 처리 중 오류가 발생했습니다!")
    else:
        print("회원정보 변경에 성공했습니다!")
        query_str = "SELECT memid, memname, addr FROM `members`"
        query_str += " WHERE memid = ?"
        cur.execute(query_str, (in_memid,))

        cur.execute(query_str, (in_memid,))
        result = cur.fetchone()
        print("--< 변경후 >--------------------------")
        print("회원 ID : ", result[0])
        print("회원이름 : ", result[1])
        print("회원주소 : ", result[2])
    finally:
        print("실행마침")
else:   # 검색한 결과가 없는 경우
    print("실입력한 회원 ID를 가지는 회원정보가 없습니다.")

# 단계 8: 프로그램 종료하기
cur.close()
conn.close()
