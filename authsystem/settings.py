"""
Django settings for authsystem project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import django_heroku
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG') == 'False'
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
 
ALLOWED_HOSTS = [' 127.0.0.1','blogapp-backend.herokuapp.com']

CORS_ORIGIN_WHITELIST = ['https://blogapp-3f83.onrender.com']

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "debug_toolbar",
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',
    'accounts',
    'payments',
    'blogposts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'authsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'build')],
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

WSGI_APPLICATION = 'authsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#New Configurations

#Custom User Configuration
AUTH_USER_MODEL = 'accounts.UserAccount'

#Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

#Database Configuration
#   DATABASES = {
#       'default' : {
#               'ENGINE'   : 'django.db.backends.postgresql',
#               'NAME'     : 'db_name',
#               'USER'     : 'user_name',
#               'PASSWORD' : 'Password' , 
#               'HOST'     : 'localhost', 
#        } 
#   }



DOMAIN = 'https://blogapp-3f83.onrender.com/'

SITE_URL = 'https://blogapp-3f83.onrender.com/acknowledge/payment/'


#Djoser Configurations
DJOSER = { 
    'LOGIN_FIELD': 'email' ,
    'USER_CREATE_PASSWORD_RETYPE': True ,
    'SEND_CONFIRMATION_EMAIL'  : True ,
    'SEND_ACTIVATION_EMAIL' : True ,
    'ACTIVATION_URL' : 'activate/{uid}/{token}',
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True ,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True ,
    'SET_USERNAME_RETYPE' : True ,
    'SET_PASSWORD_RETYPE' : True ,
    'PASSWORD_RESET_CONFIRM_URL' : 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_RETYPE' : True,
    'USERNAME_RESET_CONFIRM_URL' : 'email/reset/confirm/{uid}/{token}',
    'LOGOUT_ON_PASSWORD_CHANGE'  : True ,
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND' : True,
    'USERNAME_RESET_SHOW_EMAIL_NOT_FOUND' : True,
    'SERIALIZERS': {
        'user_create':'accounts.serializers.UserCreateSerializer',
        'user':'accounts.serializers.UserCreateSerializer',
        'user_create':'djoser.serializers.UserDeleteSerializer',
    }
}

#Rest Framework Configurations
REST_FRAMEWORK = { 
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

#Stripe Configurations

django_heroku.settings(locals())