from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_verification_email(user):
    token = generate_activation_token(user)
    uid = encode_uid(user)
    activation_link = f"http://127.0.0.1:8000{reverse('verify-email', kwargs={'uidb64': uid, 'token': token})}"

    subject = "이메일 인증"
    message = f"아래 링크를 클릭하여 이메일을 인증하세요:\n{activation_link}"
    
    send_mail(subject, message, 'sulmeulliae@gamil.com', [user.email])

def generate_activation_token(user):
    return default_token_generator.make_token(user)

def encode_uid(user):
    return urlsafe_base64_encode(force_bytes(user.pk))

