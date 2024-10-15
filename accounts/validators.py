from .models import User
import re


def check_date_format(input_date):
    # 날짜 형식 정규 표현식
    regex = r"\d{4}-\d{2}-\d{2}"
    return bool(re.match(regex, input_date))


def validate_email_format(email):
    # 이메일 형식 정규 표현식
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None


def validate_user_data(user_data):
    username = user_data.get("username")
    password = user_data.get("password")
    fullname = user_data.get("fullname")
    nickname = user_data.get("nickname")
    email = user_data.get("email")
    birth = user_data.get("birth")

    err_msg = []

    birth_year = int(birth.split("-")[0])

    # 조건과 에러 메시지를 쌍으로 묶어 두 개의 리스트에 저장
    checks = [
        (birth_year > 2005, "가입불가 미성년자입니다."),
        (
            User.objects.filter(username=username).exists(),
            "이미 존재하는 username 입니다.",
        ),
        (
            User.objects.filter(nickname=nickname).exists(),
            "이미 존재하는 nickname 입니다.",
        ),
        (not check_date_format(birth), "유효하지 않은 날짜 형식입니다.(YYYY-MM-DD)"),
    ]

    # 반복문을 통해 조건 검사 및 메시지 추가
    for condition, message in checks:
        if condition:
            err_msg.append(message)

    if not validate_email_format(email):
        err_msg.append("유효하지 않은 이메일 형식입니다.")

    # elif User.objects.filter(email=email).exists():
    #     err_msg.append("이미 존재하는 email 입니다.")

    # 에러 메시지가 있는 경우 반환
    if err_msg:
        return err_msg
