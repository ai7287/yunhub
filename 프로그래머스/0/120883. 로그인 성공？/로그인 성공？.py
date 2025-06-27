def solution(id_pw, db):
    for user in db:
        if user[0] == id_pw[0]:  # 아이디가 일치하는 경우
            if user[1] == id_pw[1]:  # 비밀번호도 일치
                return "login"
            else:  # 아이디만 일치
                return "wrong pw"
    return "fail"  # 아이디가 아예 없음
