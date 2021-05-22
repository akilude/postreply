"""

    Author        : Jagat Iyer
    Developer    : Prasanna Vijayan
    Date        : 14th Jan 2015
    Django Ver    : 1.7.1
    Projct Name    : PostReplyPrasanna

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)
print BASE_DIR

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'akashsathya@everycrave.me'
EMAIL_HOST_PASSWORD = 'akashs/osathyamurthy'
EMAIL_USE_TLS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '19z6h6xc)83=95*=-2+lmzr0$ysf$7n9bq_gpa12en52)ca#ts'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'templates/media/')

print MEDIA_ROOT

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'postandreply',    
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

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',    
)

LOGIN_REDIRECT_URL = '/home/'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


ACCOUNT_ACTIVATION_DAYS = 2