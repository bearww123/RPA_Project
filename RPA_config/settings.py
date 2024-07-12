# RPA_프로젝트 설정파일

# 파일의 자세한 내용
# https://docs.djangoproject.com/en/5.0/topics/settings/
# 설정 및 해당 값의 전체 목록
# https://docs.djangoproject.com/en/5.0/ref/settings/

from pathlib import Path
import pymysql

# BASE_DIR / 'subdir'과 같이 프로젝트 내부에 경로를 빌드합니다.
BASE_DIR = Path(__file__).resolve().parent.parent

# 빠른 개발 설정 - 프로덕션에 낮은 적합성
# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 보안 - 프로덕션 키 [ ※ 비밀 유지 해야함 ]
SECRET_KEY = "django-insecure-vog2eglb$oiut@2mddfjui#nv%s%unk+614(e+a)co7$g0e#c="
# 보안 - 프로덕션 환경 [ ※ 디버그 환경에서 실행 불가 ]
DEBUG = True
ALLOWED_HOSTS = []


# 애플리케이션 정의
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "RPA_config.urls"

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

WSGI_APPLICATION = "RPA_config.wsgi.application"

# MySQL_DB - [ DOCKER ]
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rpa_databases',
        'USER': 'root',
        'PASSWORD': 'globalm',
        'HOST': '192.168.219.110',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "RPA_static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
