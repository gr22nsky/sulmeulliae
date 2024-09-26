from .models import User
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
import re

def check_date_format(input_date):
	regex = r'\d{4}-\d{2}-\d{2}'
	return  bool(re.match(regex, input_date))

def validate_user_data(user_data):
    
    username = user_data.get("username")
    password = user_data.get("password")
    fullname = user_data.get("fullname")
    nickname = user_data.get("nickname")
    email = user_data.get("email")
    birth = user_data.get("birth")
        
    birth_year = int(birth.split('-')[0])
        
    if birth_year > 2005:
        return "가입불가 미성년자입니다"

    if User.objects.filter(nickname=nickname).exists():
        return "이미 존재하는 nickname 입니다."
    
    if User.objects.filter(email=email).exists():
        return "이미 존재하는 email 입니다."
    
    validator = EmailValidator()
    try:
        validator(email)
    except ValidationError:
        return "유효하지 않은 이메일 형식입니다."

    if not check_date_format(birth):
        return "유효하지 않은 날짜 형식입니다.(YYYY-MM-DD)"