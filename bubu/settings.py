import dj_database_url
from decouple import Csv, config
from unipath import Path
import os

PROJECT_DIR = Path(__file__).parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'storages',
    'social_django',
    'bubu.activities',
    'bubu.articles',
    'bubu.authentication',
    'bubu.core',
    'bubu.feeds',
    'bubu.messenger',
    'bubu.questions',
    'bubu.search',
    'bubu.products',
    'crispy_forms'
)

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
)

ROOT_URLCONF = 'bubu.urls'

WSGI_APPLICATION = 'bubu.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'debug': DEBUG
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = '482173618798027'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '5ca728bac5ab02a4207298181ebdfed4'  # App Secret

SOCIAL_AUTH_TWITTER_KEY = 'YHSQclrmiYPJ2rj9wulO9MorK'
SOCIAL_AUTH_TWITTER_SECRET = 'ItdLgnxHBCMMUhXoIy22CmGBDZMOnzomB7jcCFRNtEiScFtgYD'

#Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
CF_COOKIE_SECURE=True


#Set this to True to avoid transmitting the session cookie over HTTP accidentally.
SESSION_COOKIE_SECURE=True

CSRF_COOKIE_HTTPONLY=True


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Portuguese'),
    ('es', 'Spanish')
)

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
AWS_ACCESS_KEY_ID =config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'gelem-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bubu/static'),
]

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIAFILES_LOCATION = 'gelem-static/media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'bubu.storage_backends.MediaStorage'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
MEDIA_ROOT=MEDIA_URL
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#django-crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'


LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/feeds/'

ALLOWED_SIGNUP_DOMAINS = ['*']

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644
