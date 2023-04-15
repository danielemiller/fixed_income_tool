# backend/config/settings.py
from pathlib import Path
import sys
import supabase_py
import importlib.util

# Load the .db_config.py file
spec = importlib.util.spec_from_file_location("db_config", Path(__file__).resolve().parent / ".db_config.py")
db_config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(db_config)

SUPABASE_URL, SUPABASE_API_KEY, PG_NAME, PG_USER, PG_PW, PG_HOST, PG_PORT = (
    db_config.SUPABASE_URL,
    db_config.SUPABASE_API_KEY,
    db_config.PG_NAME,
    db_config.PG_USER,
    db_config.PG_PW,
    db_config.PG_HOST,
    db_config.PG_PORT,
)

supabase = supabase_py.create_client(SUPABASE_URL, SUPABASE_API_KEY)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fixed_income'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'data_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PG_NAME,
        'USER': PG_USER,
        'PASSWORD': PG_PW,
        'HOST': PG_HOST, 
        'PORT': PG_PORT,
    }
}

if 'test' in sys.argv:
    DATABASES['default']['NAME'] = ':memory:'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

