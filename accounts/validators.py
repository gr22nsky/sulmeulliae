from .models import User

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