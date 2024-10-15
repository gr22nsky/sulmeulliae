from pathlib import Path
from datetime import timedelta
import os
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()
# BASE_DIR 설정 (프로젝트의 루트 디렉토리)
BASE_DIR = Path(__file__).resolve().parent.parent

# 환경 변수 설정
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
# Set the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# # Take environment variables from .env file
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')
print(DEBUG)
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')
OPEN_API_KEY = env('OPENAI_API_KEY')
DEEPL_API_KEY= env('DEEPL_API_KEY')
# ALLOWED_HOSTS = ['api.sulmeulliae.com', '43.201.83.17', 'sulmeulliae.com', '127.0.0.1']


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party apps
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_extensions",
    'channels',
    "debug_toolbar",
    "corsheaders",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # local apps
    "accounts",
    "evaluations",
    "community",
    "chatbot",
    "chat",
]

SITE_ID = 1


ACCOUNT_AUTHENTICATIONS_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "allauth.account.middleware.AccountMiddleware", 
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "dev": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}
DATABASES['default'] = DATABASES['dev' if DEBUG else 'production']


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'sulmeulliae@gmail.com'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FORM_EMAIL = EMAIL_HOST_USER
ACCOUNT_EMAIL_CONFIRMATION_EXPORE_DAYS = 1
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[이메일 인증]'


AUTH_USER_MODEL = "accounts.User"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
    
]


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
}
SIMPLE_JWT = {
    # "ACCESS_TOKEN_LIFETIME":timedelta(minutes=5),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STATIC_URL = env("STATIC_URL", default="/static/")
# STATICFILES_DIRS = [BASE_DIR / "static"]
# STATIC_ROOT = env("STATIC_ROOT", default=BASE_DIR / "staticfiles")

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Media files
# MEDIA_URL = env("MEDIA_URL", default="/media/")
# MEDIA_ROOT = env("MEDIA_ROOT", default=BASE_DIR / "media")
MEDIA_URL = '/media/'  # 미디어 파일을 접근할 URL 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 미디어 파일이 저장될 디렉토리 경로
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS_ALLOWED_ORIGINS = [
#     'https://localhost:3000',
#     'https://api.sulmeulliae.com',
#     'https://sulmeulliae.com'
# ]
CORS_ALLOW_ALL_ORIGINS = True


OPENAI_API_KEY = env('OPENAI_API_KEY')


CSRF_TRUSTED_ORIGINS = [
    'https://api.sulmeulliae.com',
    'https://sulmeulliae.com',
    "http://localhost:3000",  # WebSocket 요청을 허용하는 프론트엔드 URL
]

# ASGI 설정
ASGI_APPLICATION = 'backend.asgi.application'

# Channels Layer 설정 
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
