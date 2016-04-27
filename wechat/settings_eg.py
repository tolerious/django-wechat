"""
Django settings for wechat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_SRC_ROOT = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z@18@fhhc@q&-v%p8o&$iiah1a(0r1-7n8v95pr=wjij)st$51'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ("*",)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_weixin'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wechat.urls'

WSGI_APPLICATION = 'wechat.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wechat',
        'USER': 'root',
        'PASSWORD': 'fenghelong',
        'HOST': 'localhost',
        'PORT': '3306',
        'CONN_MAX_AGE': 600,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '..', 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '..', 'media')
MEDIA_URL = '/media/'
LOG_FILENAME = 'django.wechat.log'
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(levelname)s: %(asctime)s %(module)s %(process)d %(thread)d %(message)s %(filename)s:%(funcName)s:%(lineno)d'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
        },
    },
    'loggers': {
        'django.request': {
            'propagate': True,
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
APP_URL = "http://chat.meiparking.com"
APP_ID = "wfelkjlsjdlf"
APP_SECRET = "sdfjljwlkejlkksdf"
AES_KEY = "klsdjfkljlksdf"
WX_TOKEN = "tolerious"
MARKET_NUMBER = "123123123"

